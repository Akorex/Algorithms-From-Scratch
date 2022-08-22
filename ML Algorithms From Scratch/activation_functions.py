from turtle import forward
import numpy as np
from math import exp as e

class ReLU:
    def forward(self, inputs):
        self.output = np.maximum(inputs, 0)
        return self.output

class Sigmoid:
    def forward(self, inputs):
        self.output = 1 / (1 + np.exp(-inputs))
        return self.output


# naive implementation without numpy
def relu_2d(x):
    """An implementation of the ReLU activation function
    Expects x to be a rank-2 numpy tensor

    ReLU is defined as: max(x, 0)
    Returns x if x > 0, 0 otherwise

    In numpy, would be x = np.maximum(x, 0.)
    """
    assert len(x.shape) == 2
    x = x.copy() # avoid overwriting tensor

    x = x.astype(np.float32)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] = max(x[i, j], 0)
    return x

def sigmoid(x):
    """An impementation of the sigmoid activation function
    
    Expects x to be a rank-2 numpy tensor
    Returns the sigmoid of x
    """
    assert len(x.shape) == 2
    x = x.copy() # avoid overwriting tensor

    x = x.astype(np.float32)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            temp = x[i, j] * -1
            x[i, j] = 1/ (e(temp) + 1)
    return x

def softmax(x):
    """An implementation of the softmax activation function
    Expects x to be a rank-2 numpy tensor
    
    Returns the normalized values for x
    """
    assert len(x.shape) == 2
    x = x.copy() # avoid overwriting tensor
    
    x = x.astype(np.float32)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] = e(x[i, j]) / sum(e(x))
    return x

x = [[1, 2, -3, 4], [1, 0, 0, 4]]
x = np.array(x)
print(x)

y = sigmoid(x)
print(y)

s = Sigmoid()
y = s.forward(x)
print(y)
