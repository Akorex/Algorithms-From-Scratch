"""

This is a code implementation of learning curves with sklearn. 
Learning curves are plots of the model's performance on the training set and the test set. 
This allows us to visualize how the model perform and could easily tell if the model is overfitting 
or underfitting. Very similar to plotting train/val loss in Deep Learning. 

A good approach to visualize where overfitting begins in training
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def plot_learning_curves(model, X, y):
    """
    Function to plot a learning curve.
    :param model: this is the sklearn model to fit to the train/val or test set
    :param X: this is the set of features
    :param y: the target the model will try to predict
    :return: a plot of the learning curve of train/test
    """

    # split the dataset
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
    train_errors, val_errors = [], []

    for m in range(1, len(X_train)):
        model.fit(X_train[:m], y_train[:m]) # fit the model up to that point in the dataset
        y_train_predict = model.predict(X_train[:m])
        y_val_predict = model.predict(X_val[:m])
        train_errors.append(mean_squared_error(y_train[:m], y_train_predict))
        val_errors.append(mean_squared_error(y_val[:m], y_val_predict))

    # a plot of the rmse for the train and validation set
    plt.plot(np.sqrt(train_errors), 'bo+', label = 'Training Error')
    plt.plot(np.sqrt(val_errors), 'b-', label = 'Validation Error')