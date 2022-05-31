"""
Contains necessary codes used for modelling with sci-kit learn, XGBoost, 
LGBM and other libraries

General code requirements:
1. code dependencies other than numpy, pandas, matplotlib and seaborn are imported 
within functions when used
2. Require dataframes in place of numpy arrays 
3. function docs should state explicitly if (1) is otherwise
4. Returns dataframes when possible
5. docs state explicitly when numpy arrays is returned

File contains two high computation functions: which trains LGBM and XGBOOST classifiers
using cross validation and encoding (for the LGBM model only) schemes.

and two three computation functions: which trains LGBM and XGBOOST classifiers without the 
cross validation schemes as explained above and a simple model which trains an sklearn model with
cross validation.
"""
# import dependencies
from lightgbm import LGBMClassifier
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

def train_model_lgbm(features, test_features, target, encoding='ohe', n_folds=5):
    """ Full function to train an LGBM model with encoding 
    and cross validation schemes 
    Args:
        features: pandas dataframe of train features with target
        test_features: pandas dataframe of test features
        target: string name of the target column
        encoding: encoding scheme to use, usually 'ohe' (default) or 'le'
        n_folds: number of folds for cross validation. defaults to 5
             
    Returns:
           Feature importance, submission and metric dataframes 
    """
    from sklearn.preprocessing import LabelEncoder
    from sklearn.model_selection import KFold
    import gc

    labels = features[target]
    features = features.drop(columns=[target])
    ids = test_features['ids']

    # encode the categorical features
    if encoding == 'ohe':
        features = pd.get_dummies(features)
        test_features = pd.get_dummies(test_features)
        features, test_features = pd.align(features, test_features, join='inner', axis=1)
        cat_indices = 'auto'

    elif encoding == 'le':
        encoder = LabelEncoder()
        cat_indices = []

        for i, col in enumerate(features):
            if features[col].dtype == 'object':
                cat_indices.append(i)
                features[col] = encoder.fit_transform(features[col])
                test_features[col] = encoder.fit_transform(test_features[col])
    else:
        raise ValueError("Encoding must be either 'ohe' or 'le'")

    # get column names
    columns = list(features.columns)

    # convert to numpy array
    features = np.array(features)
    test_features = np.array(test_features)
    labels = np.array(labels)

    # create the kfold object
    kfold = KFold(n_splits=n_folds, shuffle=False)

    # Empty array for feature importances and test predictions
    feature_importance_values = np.zeros(len(features))
    test_predictions = np.zeros(test_features.shape[0])
    
    # empty array for out of fold predictions
    out_of_fold = np.zeroes(features.shape[0])

    # metrics
    valid_scores = []
    train_scores = []

    for train_index, test_index in kfold.split(features):
        train_features, train_labels = features[train_index], labels[train_index]
        valid_features, valid_labels = features[test_index], labels[test_index]

        model = LGBMClassifier(n_estimators=1000, objective='binary', class_weight='balanced', 
        reg_alpha=0.1, reg_lambda=0.1, n_jobs=-1, random_state=42, learning_rate=0.05)

        model.fit(train_features, train_labels, eval_metric = 'auc',
                  eval_set = [(valid_features, valid_labels), (train_features, train_labels)],
                  eval_names = ['valid', 'train'], categorical_feature = cat_indices, early_stopping_rounds=100, verbose=200)
        
        best_iteration = model.best_iteration_

        feature_importance_values += model.feature_importances_ / kfold.n_splits
        test_predictions += model.predict(test_features, num_iteration=best_iteration)/kfold.n_splits

        out_of_fold[test_index] = model.predict(valid_features, num_iteration = best_iteration)
        valid_score = model.best_score_['valid']['auc']
        train_score = model.best_score_['train']['auc']

        valid_scores.append(valid_score)
        train_scores.append(train_score)

    # Overall validation score
    valid_auc = roc_auc_score(labels, out_of_fold)
    # Add the overall scores to the metrics
    valid_scores.append(valid_auc)
    train_scores.append(np.mean(train_scores))
    
    # Needed for creating dataframe of validation scores
    fold_names = list(range(n_folds))
    fold_names.append('overall')

    # clear memory
    gc.enable()
    del model, train_features, valid_features
    gc.collect()

    # make feature importances, submission and dataframe
    feature_importance = pd.DataFrame({'feature': columns, 'importance': feature_importance_values})
    submission = pd.DataFrame({'ids': ids, 'target': test_predictions})
    metrics = pd.DataFrame({'fold': fold_names, 'train': train_scores,
                            'valid': valid_scores})

    return feature_importance, submission, metrics

def train_model_xgboost(features, test_features, target, n_splits=5):
    """ Full function to train an XGBClassifier model with encoding 
    and cross validation schemes 
    Args:
        features: pandas dataframe of train features with target
        test_features: pandas dataframe of test features
        target: string name of the target column
        n_splits: number of folds for cross validation. defaults to 5
    
    Requires gpu
    Returns:
           Feature importance, submission and metric dataframes 
    """
    from sklearn.preprocessing import LabelEncoder
    from sklearn.model_selection import KFold
    from sklearn.metrics import roc_auc_score
    from xgboost import XGBClassifier
    import gc

    labels = features[target]
    features = features.drop(columns=[target])
    ids = test_features['ids']

    # get column names
    columns = list(features.columns)

    # convert to numpy array
    features = np.array(features)
    test_features = np.array(test_features)
    labels = np.array(labels)

    # create the kfold object
    kfold = KFold(n_splits=n_splits, shuffle=False)

    # Empty array for feature importances and test predictions
    feature_importance_values = np.zeros(len(features))
    test_predictions = np.zeros(test_features.shape[0])
    
    # empty array for out of fold predictions
    out_of_fold = np.zeros(features.shape[0])

    # metrics
    valid_scores = []
    train_scores = []

    for train_index, test_index in kfold.split(features):
        train_features, train_labels = features[train_index], labels[train_index]
        valid_features, valid_labels = features[test_index], labels[test_index]

        model = XGBClassifier(n_estimators=1000, objective='binary:logistic', class_weight='balanced', 
        reg_alpha=0.1, reg_lambda=0.1, n_jobs=-1, random_state=42, learning_rate=0.05, tree_method='gpu_hist')

        model.fit(train_features, train_labels, eval_metric = 'auc',
                  eval_set = [(valid_features, valid_labels), (train_features, train_labels)],
                  eval_names = ['valid', 'train'], early_stopping_rounds=100, verbose=200)
        

        feature_importance_values += model.feature_importances_ / kfold.n_splits
        test_predictions += model.predict(test_features, iteration_range=(0, model.best_iteration))/kfold.n_splits

        out_of_fold[test_index] = model.predict(valid_features, iteration_range=(0, model.best_iteration))
        valid_score = model.best_score_['valid']['auc']
        train_score = model.best_score_['train']['auc']

        valid_scores.append(valid_score)
        train_scores.append(train_score)

    # Overall validation score
    valid_auc = roc_auc_score(labels, out_of_fold)
    # Add the overall scores to the metrics
    valid_scores.append(valid_auc)
    train_scores.append(np.mean(train_scores))

    # Needed for creating dataframe of validation scores
    fold_names = list(range(n_splits))
    fold_names.append('overall')

    # clear memory
    gc.enable()
    del model, train_features, valid_features
    gc.collect()

    # make feature importances, submission and dataframe
    feature_importance = pd.DataFrame({'feature': columns, 'importance': feature_importance_values})
    submission = pd.DataFrame({'ids': ids, 'target': test_predictions})
    metrics = pd.DataFrame({'fold': fold_names, 'train': train_scores,
                            'valid': valid_scores})
    
    return feature_importance, submission, metrics


def train_xgboost(X_train, y_train, X_test):
    """
    Quick function to train an XGBoost model on the training data and returns the predictions
    on the test data
    Args: 
        X_train: training data without TARGET (accepts numpy arrays or df)
        y_train: TARGET column (accepts numpy arrays or df)
        X_test: test data to make predictions on (accepts numpy arrays or df)
        
    """
    from sklearn.model_selection import train_test_split
    import xgboost as xgb
    
    X_train_xgb, X_valid, y_train_xgb, y_valid = train_test_split(X_train, y_train, train_size=0.8, random_state=42)
    
    # convert the split data to xgboost format
    d_train = xgb.DMatrix(X_train_xgb, y_train_xgb)
    d_test = xgb.DMatrix(X_valid, y_valid)
    X_test_d = xgb.DMatrix(X_test)
    
    # the parameters for training
    params_1 = {
    'booster': 'gbtree', 'max_depth': 5, 
    'learning_rate': 0.025, 'min_split_loss': 0.01, 'min_child_weight': 5,'subsample': 0.8,
    'colsample_bytree': 0.25, 'alpha': 2, 'lambda': 3, 'objective': 'binary:logistic',
    'num_class': 3, 'eval_metric':'mlogloss'
    }

    num_round = 1000
    evallist = [(d_train, 'train'), (d_test, 'eval')]
    model = xgb.train(params_1, d_train, num_round, evallist, early_stopping_rounds=20, verbose_eval=50)
    
    predictions = model.predict(X_test_d, iteration_range=(0, model.best_iteration))
    
    return predictions

def train_lgbm(X_train, y_train, X_test):
    """
    Trains an LGBM model on the training data and returns the predictions
    on the test data
    Args: 
        X_train: training data without TARGET
        y_train: TARGET
        X_test: test data to make predictions on
        
    """
    from sklearn.model_selection import train_test_split
    import lightgbm as lgb
    from sklearn.metrics import roc_auc_score
    
    X_train_lgbm, X_valid, y_train_lgbm, y_valid = train_test_split(X_train, y_train, train_size=0.8, random_state=42)
    
    # convert the split data to xgboost format
    d_train = lgb.Dataset(X_train_lgbm, y_train_lgbm)
    d_test = lgb.Dataset(X_valid, y_valid)
    X_test_d = lgb.Dataset(X_test)
    
    # the parameters for training
    params_1 = {
    'objective': 'binary', 'metric': 'binary_logloss',
    'learning_rate': 0.025, 'num_leaves': 5, 'max_depth': 5,
    'min_child_samples': 5, 'subsample': 0.8, 'colsample_bytree': 0.25,
    'alpha': 2, 'lambda': 3, 'verbose': -1
    }

    num_round = 1000
    evallist = [(d_train, 'train'), (d_test, 'eval')]
    model = lgb.train(params_1, d_train, num_round, evallist, early_stopping_rounds=20, verbose_eval=50)
    
    predictions = model.predict(X_test_d, num_iteration=model.best_iteration)
    
    return predictions

def train_model(model, X_train, y_train, X_valid, y_valid, n_splits=5):
    """trains the dataset with model using cross validation of n_splits
    Args: 
         model - model to use in training the dataset
         X_train - np array of train without the target.
         y_train - np array of target
         X_valid - np array of validation without the target
         y_valid - np array of target in validation data
         n_splits - number of splits to use in cross validation. defaults to 5
    Returns: 
            dictionary of metrics on the validation data
    """
    from sklearn.model_selection import StratifiedKFold
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    kfold = StratifiedKFold(n_splits=n_splits, random_state=42, shuffle=True)
    
    accuracy = []
    precision = []
    recall = []
    f1 = []
    for train_index, test_index in kfold.split(X_train, y_train):
        X_train_folds = X_train[train_index] 
        y_train_folds = y_train[train_index]
        X_valid_folds = X_train[test_index]
        y_valid_folds = y_train[test_index]
        
        model.fit(X_train_folds, y_train_folds)
        y_pred = model.predict(X_valid_folds)
        
        accuracy.append(accuracy_score(y_valid_folds, y_pred))
        precision.append(precision_score(y_valid_folds, y_pred))
        recall.append(recall_score(y_valid_folds, y_pred))
        f1.append(f1_score(y_valid_folds, y_pred))
    
    accuracy = round(sum(accuracy)/len(accuracy), 2)
    precision = round(sum(precision)/len(precision), 2)
    recall = round(sum(recall)/len(recall), 2)
    f1 = round(sum(f1)/len(f1), 2)

    y_pred = model.predict(X_valid)
    valid_accuracy = round(accuracy_score(y_valid, y_pred), 2)
    valid_precision = round(precision_score(y_valid, y_pred), 2)
    valid_recall = round(recall_score(y_valid, y_pred), 2)
    valid_f1 = round(f1_score(y_valid, y_pred), 2)
    
    metrics = {}
    metrics['accuracy'] = valid_accuracy
    metrics['precision'] = valid_precision
    metrics['recall'] = valid_recall
    metrics['f1'] = valid_f1

    print(f"train accuracy: {accuracy}\t\t validation accuracy: {valid_accuracy}")
    print(f"train precision: {precision}\t\t validation precision: {valid_precision}")
    print(f"train recall: {recall}\t\t validation recall: {valid_recall}")
    print(f"train f1: {f1}\t\t validation f1: {valid_f1}")
    return metrics