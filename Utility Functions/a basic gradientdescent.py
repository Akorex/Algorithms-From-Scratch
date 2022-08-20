import numpy as np # for numerical calculations
import matplotlib.pyplot as plt


""""

This is an implementation of different approaches to gradient descent for regression
"""

# a simple linear equation -- check normalequation file to see plot
X = 2 * np.random.rand(100, 1)
y = 4 + 3*X + np.random.randn(100, 1)
X_b = np.c_[np.ones((100, 1)), X] #add x0 = 1 to each instance of X

m = 100 # number of training samples

def basic_gdescent(theta):
    # set some parameters to define gradient descent
    eta = 0.1 # the learning rate
    n_iterations = 1000

    for iteration in range(n_iterations):
        gradient = 2/m * X_b.T.dot(X_b.dot(theta) - y)
        theta = theta - eta * gradient
        
    return theta

def learning_schedule(t):
    t0, t1 = 5, 50 # learning hyperparameters
    
    return t0/(t + t1)

def stochastic_gdescent(theta):
    n_epochs = 50 # number of epochs
    plt.figure(figsize=(12, 8)) # create a new plot

    for epoch in range(n_epochs):
        for i in range(m):
            random_index = np.random.randint(m)
            xi = X_b[random_index: random_index + 1]
            yi = y[random_index: random_index + 1]
            gradient = 2 * xi.T.dot(xi.dot(theta) - yi)
            eta = learning_schedule(epoch * m + i) # define the learning rate

            theta = theta - eta*gradient

        # make a new prediction and visualize how stochastic gradient performed
        X_new = np.array([[0], [2]])
        X_c = np.c_[np.ones((2, 1)), X_new] #add x0 = 1 to each instance of X
        y_predict = X_c.dot(theta) # make the prediction at each epoch

        plt.plot(X_new, y_predict, 'b-')
        plt.plot(X, y, 'b.')
        plt.axis([0, 2, 0, 15])

    print(theta)
    plt.show()

if __name__ == '__main__':

    # a random initialization
    theta = np.random.randn(2, 1) 
    
    print(basic_gdescent(theta))
    stochastic_gdescent(theta)