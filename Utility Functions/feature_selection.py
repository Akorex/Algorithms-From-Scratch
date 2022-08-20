"""
This python file contains utility functions to carry out feature selection 
in the Machine Learning pipeline. 

General code requirements:
1. code dependencies other than numpy, pandas, matplotlib and seaborn are imported 
within functions when used
2. Require dataframes in place of numpy arrays 
3. function docs should state explicitly if (1) is otherwise
4. Returns dataframes when possible
5. docs state explicitly when numpy arrays is returned
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

from sklearn.feature_selection import mutual_info_regression
from sklearn.feature_selection import SelectKBest, chi2

def select_kbestfeatures(X_train, y_train, X_test, score_func = chi2, k = 5, transform = 1):
    """Uses scikit-learn's SelectKBest to perform feature selection of columns
    
    Args:  
        X_train: df of features in the train dataset, without the target
        y_train: df of the target set in the train dataset
        X_test: df of features in the test dataset without the target
        score_func: used to score the features for univariate classification, defaults to chi2 score
        k : number of features to select, defaults to 5
        transform: decides if to transform X_train in terms of the kbest features. 1/0

    Returns:
           prints a df of best features in order of descending scores
           if transform, returns dataframes of  X_train and X_test
            with only the features selected
    """  
    bestfeatures = SelectKBest(score_func=score_func, k=k)
    bestfeatures.fit(X_train, y_train)

    scores = pd.Series(bestfeatures.scores_)
    columns = pd.Series(X_train.columns)

    # concat
    df = pd.concat([columns, scores], axis=1)
    df = df.rename(columns={0: 'Columns', 1: 'Scores'})
    display(df.sort_values(by='Scores', ascending=False))

    if transform == 1:
        X_train = bestfeatures.transform(X_train)
        X_test = bestfeatures.transform(X_test)

        X_train = pd.DataFrame(X_train, columns=bestfeatures.get_feature_names_out())
        X_test = pd.DataFrame(X_test, columns=bestfeatures.get_feature_names_out())
    elif transform == 0:
        X_train = X_train.copy()
        X_test = X_test.copy()
    else:
        raise ValueError('transform must be 0 or 1')
    return X_train, X_test

def mututalinfo_scores(X_train, y_train):
    """computes the mutual info scores for regression for features in X_train scores 
    can be combined with select_KBEST to perform feature selection.

    Args:
         X_train: df of train without target
         y_train: df of target
    Returns a pandas Series of mutual info scores of the columns
    """
    discrete_features = X_train.dtypes == int 
    mi_scores = mutual_info_regression(X_train, y_train, discrete_features=discrete_features, random_state=42)

    # make a pandas Series with these scores
    mi_scores = pd.Series(mi_scores, name='mutual_info scores', index=X_train.columns)
    mi_scores = mi_scores.sort_values(ascending=False)
    return mi_scores

def plot_mi_scores(mi_scores):
    """returns a plot of the mutual_info scores returned by the mutualinfo_scores function"""
    scores = mi_scores.sort_values(ascending=True)
    width = np.arange(len(scores))
    ticks = list(scores.index)
    plt.figure(figsize=(20, 10))
    plt.barh(width, scores)
    plt.yticks(width, ticks)
    plt.title('Mututal information scores')

    plt.show()

def cross_val_class(X_train,y_train,classifier_list,classifier_name,scoring):
    """
    run quick cross validation
    params :
            :- classifier_list = array of models 
                    e.g >>> model = [AdaBoostClassifier(),RandomForestClassifier(n_estimators=50,max_leaf_nodes=25)]
            
            :- classifier_name = array (description of the model)
                    e.g >>> model_name= ['AdaBoostClassifier()','RandomForestClassifier','xg','et','lr','nb_m','dr']
                    
            Use sorted(sklearn.metrics.SCORERS.keys()) to get valid options.

    """
    from sklearn.model_selection import cross_val_score,StratifiedShuffleSplit
    #kf=StratifiedShuffleSplit()
    mod=[]
    cv_score=[]
    for m in classifier_list:
        cv_score.append(cross_val_score(m,X_train,y_train,scoring=scoring,cv=5))
        #score = np.sqrt(score)
    cross_val = pd.DataFrame(cv_score,index=classifier_name)
    return cross_val

def remove_missing_columns(train, test, threshold=90):
    """Computes the percent of missing values of each columns in the dataframes 
    and removes columns with percent of missing values above threshold

    Returns:
           train and test dataframes with columns with missing_values percent > threshold dropped
    """
    train_miss = pd.DataFrame(train.isnull().sum())
    train_miss['percent'] = 100 * train_miss[0] / len(train)

    test_miss = pd.DataFrame(test.isnull().sum())
    test_miss['percent'] = 100 * test_miss[0] / len(test)

    # list of missing columns above threshold
    missing_train_columns = list(train_miss.index[train_miss['percent'] > threshold])
    missing_test_columns = list(test_miss.index[test_miss['percent'] > threshold])

    # combine the two lists together
    missing_columns = list(set(missing_train_columns + missing_test_columns))
    print(f"There are {len(missing_columns)} columns with percent of missing columns higher than {threshold}%")

    train = train.drop(columns=missing_columns)
    test = test.drop(columns = missing_columns)

    return train, test

def remove_collinear_features(train, test, threshold=0.8):
    """Computes the correlation matrix for the train dataset and removes highly collinear features

    above_threshold_features = {feature1: (feature1, feature2, feature3), etc}
    where feature1, feature2, feature3 are features very highly correlated with feature1 (feature1 trivially so as corr=1)
    
    Returns: 
            train & test dataframes with highly correlated features dropped
            """
    corr = train.corr()  # compute the correlation matrix
    above_threshold_features = {} # dictionary to hold highly correlated features
    # record only correlations above threshold
    for col in corr:
        above_threshold_features[col] = list(corr.index[corr[col] > threshold]) 
    
    cols_to_remove = []
    cols_seen = []
    cols_to_remove_pair = []

    for key, value in above_threshold_features.items():
        cols_seen.append(key)
        
        for x in value:
            if x == key:
                next
            else:
                # only remove one in a pair
                if x not in cols_seen:
                    cols_to_remove.append(x)
                    cols_to_remove_pair.append(key)
    
    cols_to_remove = list(set(cols_to_remove))
    print('Number of columns to remove: ', len(cols_to_remove))

    train = train.drop(columns=cols_to_remove)
    test = test.drop(columns=cols_to_remove)

    return train, test

def permutation_importance(X_train, y_train, model):
    """Computes permutation importance for the features in train
    using the ML library eli5
    Permutation Importance works by shuffling the values in a single column, making predictions with new dataset
    and then calculating how the loss function deteriorated due to shuffling.
    Then unshuffling and applying to other columns in the dataframe
    
    Returns a df of columns by their permutation importance scores
    """
    # import the library
    import eli5
    from eli5.sklearn import PermutationImportance

    perm = PermutationImportance(model, random_state=42).fit(X_train, y_train)
    result = eli5.show_weights(perm, feature_names=X_train.columns.tolist())

    return result

def shap_values(X_train, y_train, model):
    """Computes Shapley values () for the features in X_train using SHAP library

    To get the importance of feature X{i}:
    Get all subsets of features S that do not contain X{i}
    Compute effect on our predictions of adding X{i} to all those subsets
    Aggregate all contributions to compute the marginal contribution of the feature

    Beta mode
    """

    import shap
    shap.initjs() # initialize shap

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_train)

    i = 4776 # the row to plot
    shap.force_plot(explainer.expected_value, shap_values[i], features=X_train.loc[i], feature_names=X_train.columns)
    shap.summary_plot(shap_values, features=X_train, feature_names=X_train.columns)

def remove_low_variance(X_train, X_test, threshold=0.1):
    """Computes the variance for each feature in the train set 
    Drops features in train and test with very low variance, not up to threshold
    Args:
         X_train = df of train set without the target
         X_test = df of the test set without the target
        threshold = the threshold for variance

    Returns: dataframes X_train and X_test with low variance features dropped
    """
    from sklearn.feature_selection import VarianceThreshold

    var_thresh = VarianceThreshold(threshold=threshold)
    var_thresh.fit(X_train)
    X_train = var_thresh.transform(X_train)
    X_test = var_thresh.transform(X_test)

    X_train = pd.DataFrame(X_train, columns=var_thresh.get_feature_names_out())
    X_test = pd.DataFrame(X_test, columns=var_thresh.get_feature_names_out())
    
    return X_train, X_test