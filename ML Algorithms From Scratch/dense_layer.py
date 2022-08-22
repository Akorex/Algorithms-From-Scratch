import numpy as np
import nnfs
from nnfs.datasets import spiral_data
from activation_functions import ReLU

nnfs.init() # sets random seed to 0, creates a float32 dtype default

class Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 *np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        self.activation = ReLU()

    def forward(self, inputs):
        self.output = self.activation.forward(np.dot(inputs, self.weights) + self.biases) # (inputs.shape[0], self.weights.shape[1])
        return self.output

if __name__ == '__main__':
    X, y = spiral_data(100, 3)
    dense = Dense(2, 3)

    print(dense.forward(X))