"""
Author: Akorede Adewole, 2022.
Implementation of a simple neural network with user-defined functions
"""

import numpy as np
from nnfs.datasets import spiral_data
from activation_functions import ReLU, Softmax
from dense_layer import Dense
from loss import CategoricalCrossEntropy, SparseCategoricalCrossEntropy
import nnfs 

nnfs.init() # sets random seed to 0, creates a float32 dtype default
X, y = spiral_data(100, 3)

# layer 1
relu = ReLU()
dense = Dense(2, 3, relu)
layer1_output = dense.forward(X) # (100, 3)


# layer 2
relu = ReLU()
dense = Dense(3, 4, relu)
layer2_output = dense.forward(layer1_output)  # (100, 4)


# layer 3
softmax = Softmax()
dense = Dense(4, 3, softmax)
layer3_output = dense.forward(layer2_output)
print(layer3_output[:3])

# loss function
print(y.shape) # (300,)
loss = SparseCategoricalCrossEntropy()
loss_value = loss.calculate(layer3_output, y)
print(loss_value)