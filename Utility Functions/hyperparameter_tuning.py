"""
File contains functions, code required for hyperparameter tuning 
with the Sci-kit learn, optuna and other methods

General code requirements:
1. code dependencies other than numpy, pandas, matplotlib and seaborn are imported 
within functions when used
2. Require dataframes in place of numpy arrays 
3. function docs should state explicitly if (1) is otherwise
4. Returns dataframes when possible
5. docs state explicitly when numpy arrays is returned
"""
import optuna
from optuna import Trial
from sklearn.metrics import accuracy_score

def objective(trial:Trial, train, target, test, score = accuracy_score):
    """Trains the train dataset with XGBClassifier
    Returns score to be optimized by optuna
    Args:
        Trial: the optuna object
        train: dataframe without target to train the algorithm on
        target: the values to predict
        test: dataframe to predict values of target for
        score: the metric to optimize with optuna. default's to sci-kit learn's accuracy score

    """

    # import required dependencies
    import xgboost as xgb
    from sklearn.model_selection import train_test_split

    # define the params for tuning
    params = { 
        'objective': trial.suggest_categorical('objective','binary:logistic'),
        'alpha': trial.suggest_loguniform('alpha',1e-3,10.0),
        'tree_method': trial.suggest_categorical('tree_method',['gpu_hist']),  # to use gpu
        'eval_metric': trial.suggest_categorical('eval_metric', score),
        'colsample_bytree': trial.suggest_uniform('colsample_bytree', 0.3,1.0),
        'subsample': trial.suggest_uniform('subsample', 0.4, 1.0),
        'learning_rate': trial.suggest_loguniform('learning_rate', 0.001,0.1)
    }
    
    # drop target column if present

    if 'TARGET' in train:
        train = train.drop(columns=['TARGET'])
    
    X_train, X_valid, y_train, y_valid = train_test_split(train, target, random_state=42, test_size=0.2)
    d_train = xgb.DMatrix(X_train, y_train)
    d_valid = xgb.DMatrix(X_valid, y_valid)
    d_test = xgb.DMatrix(test)
    
    num_round = 1000
    evallist = [(d_train, 'train'), (d_valid, 'eval')]

    model = xgb.train(params, d_train, num_round, evals=evallist, early_stopping_rounds=20, verbose_eval=50)
    
    y_pred = model.predict(d_test, iteration_range=(0, model.best_iteration))

    accuracy = accuracy_score(target, y_pred)

    return accuracy

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=3)