import numpy as np

# a vector of gradients from next layers
dvalues = np.array([[1., 1., 1.], 
                    [2., 2., 2.], 
                    [3., 3., 3.]])

inputs = np.array([[1., 2., 3., 3.5], 
                    [2.,5., -1., 2.], 
                    [-1.5, 2.7, 3.3, -0.8]])

weights = np.array([[0.2, 0.8, -0.5, 1], 
                    [0.5, -0.91, 0.26, -0.5], 
                    [-0.26, -0.27, 0.17, 0.87]]).T

biases = np.array([[2, 3, 0.5]])

# forward pass 
layer_outputs = np.dot(inputs, weights) + biases
relu_outputs = np.maximum(0, layer_outputs)


# start the backpropagation
drelu = relu_outputs.copy()
drelu[layer_outputs <= 0] = 0
print(drelu)

# for the dense layer
dinputs = np.dot(drelu, weights.T) # gradient of neuron function wrt weights
dweights = np.dot(inputs.T, drelu) # gradient of neuron function wrt inputs
dbiases = np.sum(drelu, axis =0, keepdims=True)

# update the parameters
weights += -0.01 * dweights
biases += -0.01 * dbiases

print(weights)
print(biases)