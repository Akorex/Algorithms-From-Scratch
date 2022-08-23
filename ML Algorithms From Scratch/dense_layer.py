"""
Author: Akorede Adewole, 2022.

This file contains implementation of the Dense layer for neural networks using numpy.
In the tf_Dense class that follows, similar implementation is done using lower TensorFlow 
code.

Implementation only for academic purposes
"""

import numpy as np
import nnfs
from nnfs.datasets import spiral_data
from activation_functions import ReLU
import tensorflow as tf

nnfs.init() # sets random seed to 0, creates a float32 dtype default

# using only numpy
class Dense:
    def __init__(self, n_inputs, n_neurons, activation):
        """Initialize the weights and biases of the Dense layer.
        
        The weights are random values drawn from a normal distribution of shape (n_inputs, n_neurons)
        The biases are initialized with a value of 0.
        Supported activation functions are: ReLU, Sigmoid, Softmax.

        For the hidden layers, the n_inputs need to match the number of rows from the output of the 
        previous layer. This is explained in the stacking_layers file.

        For the output layer, the n_neurons need to match the number of labels in the dataset.
        """
        self.weights = 0.01 *np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        self.activation = activation

    def forward(self, inputs):
        self.output = self.activation.forward(np.dot(inputs, self.weights) + self.biases) # (inputs.shape[0], self.weights.shape[1])
        return self.output

# using TensorFlow's API
class tf_Dense:
    def __init__(self, input_size, output_size, activation):
        self.activation = activation
        w_shape = (input_size, output_size)
        w_initial_value = tf.random.uniform(w_shape, minval=0, maxval=1e-1) # inialize random weights
        self.W = tf.Variable(w_initial_value)

        b_shape = (output_size, )
        b_initial_value = tf.zeros(b_shape)
        self.b = tf.Variable(b_initial_value)
    
    def __call__(self, inputs):
        return self.activation(tf.matmul(inputs, self.W) + self.b)



if __name__ == '__main__':
    X, y = spiral_data(100, 3)
    dense = Dense(2, 3)

    print(dense.forward(X))