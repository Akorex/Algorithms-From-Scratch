"""
This is a basic implementation of recursive feature elimination on some toy dataset. 
"""

from numpy import mean
from numpy import std
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt



# get the dataset

def get_dataset():
    """
    A function to grab a toy dataset from sklearn's API
    :Return: the dataset
    
     """
    X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, 
    random_state = 42)
    return X, y

# get a list of models to evaluate

def get_models():
    models = dict()

    # logistic regression
    rfe = RFE(estimator=LogisticRegression(), n_features_to_select=5)
    model = DecisionTreeClassifier()
    models['lr'] = Pipeline(steps=[('s', rfe), ('m', model)])

    # perceptron
    rfe = RFE(estimator=Perceptron(), n_features_to_select=5)
    model= DecisionTreeClassifier()
    models['per'] = Pipeline(steps=[('s', rfe), ('m', model)])

    # cart
    rfe = RFE(estimator=DecisionTreeClassifier(), n_features_to_select=5)
    model = DecisionTreeClassifier()
    models['cart'] = Pipeline(steps=[('s', rfe), ('m', model)])

    # randomforests
    rfe = RFE(estimator=RandomForestClassifier(), n_features_to_select=5)
    model = DecisionTreeClassifier()
    models['rf'] = Pipeline(steps=[('s', rfe), ('m', model)])

    # gbm
    rfe = RFE(estimator=GradientBoostingClassifier(), n_features_to_select=5)
    model = DecisionTreeClassifier()
    models['gbm'] = Pipeline(steps=[('s', rfe), ('m', model)])

    return models

# evaluate a model using cross-validation

def evaluate_model(model, X, y):
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=42)
    scores = cross_val_score(model, X, y, scoring = 'accuracy', cv=cv, n_jobs=-1)

    return scores
    

# define dataset
X, y = get_dataset()

# get models to evalaute on
models = get_models()

# evaluate the models and store results

results, names = list(), list()
for name, model in models.items():
    scores = evaluate_model(model, X, y)
    results.append(scores)
    names.append(name)

    print('>%s %.3f (%.3f)' % (name, mean(scores), std(scores)))

# plot model performance for comparison
plt.boxplot(results, labels=names, showmeans=True)
plt.show()