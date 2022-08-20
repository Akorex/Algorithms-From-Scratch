"""
This file contains utility functions to implement machine learning equations
"""
import numpy as np
import matplotlib.pyplot as plt


def normalequation():
    """
    Linear Regression can be solved using the normal equation method.
    This function implements the equation for a given input to determine its output,
    returns the prediction made by the equation and plots it using matplotlib.
    """
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3*X + np.random.randn(100, 1)
    
    X_b = np.c_[np.ones((100, 1)), X] #add x0 = 1 to each instance
    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    
    print(theta_best)
    
    # make some new prediction
    X_new = np.array([[0], [2]])
    X_new_b = np.c_[np.ones((2, 1)), X_new] # add x0 = 1 to each instance
    y_predict = X_new_b.dot(theta_best)
    print(y_predict)
    
    # plot the prediction
    plt.plot(X_new, y_predict, 'r-', label='Predictions')
    plt.plot(X, y, 'b.')
    plt.axis([0, 2, 0, 15])
    plt.legend()
    
    plt.show()