# coding a layer of neurons from scratch

inputs = [1, 2, 3, 4, 5]
weights1 = [0.2, 0.8, -0.5, 1.0, 1.2]
weights2 = [0.5, 0.1, -0.26, -0.91, 1.0]
weights3 = [-0.26, -0.27, 0.17, 0.04, 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5

outputs = [
    # neuron 1
    inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2]
    + inputs[3] * weights1[3] + inputs[4] * weights1[4] + bias1,

    # neuron 2
    inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2]
    + inputs[3] * weights2[3] + inputs[4] * weights2[4] + bias2, 

    # neuron 3
    inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2]
    + inputs[3] * weights3[3] + inputs[4] * weights3[4] + bias3
]
print("Naive Approach")
print(outputs)

## using a loop
inputs = [1, 2, 3, 4, 5]
weights = [[0.2, 0.8, -0.5, 1.0, 1.2], [0.5, 0.1, -0.26, -0.91, 1.0], [-0.26, -0.27, 0.17, 0.04, 0.87]]
biases = [2, 3, 0.5]

# output of each layer
layer_outputs = []

for neuron_weight, neuron_bias in zip(weights, biases):
    neuron_output = 0

    for n_input, weight in zip(inputs, neuron_weight):
        neuron_output += n_input * weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)
print("Using a loop")
print(layer_outputs)

## using numpy
import numpy as np
inputs = [1, 2, 3, 4, 5]
weights = [[0.2, 0.8, -0.5, 1.0, 1.2], [0.5, 0.1, -0.26, -0.91, 1.0], [-0.26, -0.27, 0.17, 0.04, 0.87]]
biases = [2, 3, 0.5]

outputs = np.dot(inputs, np.array(weights).T) + biases
print("Using numpy")
print(outputs)

## using user-defined function

from tensor_operations import matrix_vector_dot
inputs = [1, 2, 3, 4, 5]
weights = [[0.2, 0.8, -0.5, 1.0, 1.2], [0.5, 0.1, -0.26, -0.91, 1.0], [-0.26, -0.27, 0.17, 0.04, 0.87]]
biases = [2, 3, 0.5]

inputs = np.array(inputs)
weights = np.array(weights)

output = matrix_vector_dot(weights, inputs) + biases
print("Using user-defined function")
print(output)


### a batch of inputs
inputs = [[1, 2, 3, 4, 5], 
        [2, 5, -1, 0, 0], 
        [-1, 1, 5, 34, 5]]
weights = [[0.2, 0.8, -0.5, 1.0, 1.2],
        [0.5, 0.1, -0.26, -0.91, 1.0], 
        [-0.26, -0.27, 0.17, 0.04, 0.87]]
biases = [2, 3, 0.5]

print("\n")
print("A batch of inputs")
outputs = np.dot(inputs, np.array(weights).T) + biases
print(outputs)


#2
from tensor_operations import cross_product
inputs = [[1, 2, 3], 
        [2, 5, -1], 
        [-1, 1, 5]]

weights = [[0.2, 0.8, -0.5],
        [0.5, 0.1, -0.26], 
        [-0.26, -0.27, 0.17]]

inputs = np.array(inputs)
weights = np.array(weights)

output = cross_product(inputs, weights)
print("\n")
print(output)

