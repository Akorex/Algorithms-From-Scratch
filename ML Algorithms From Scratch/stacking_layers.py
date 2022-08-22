import numpy as np

inputs = [[1, 2, 3, 2.5], 
          [2.0, 5.0, -1.0, 2.0],
            [-1.5, 2.7, 3.3, -0.8]]

weights = [[0.2, 0.8, -0.5, 1.0],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

layer1_output = np.dot(inputs, np.array(weights).T) + biases
print(layer1_output)

"""
To stack layers for a neural network, we need to pay attention to the shape of the output of the first
layer and the shape of the input of the second layer. As we see from above, the neural net has 3 neurons -
(3 sets of values for weights and biases), however each weight set has 4 values. 
The output of this first layer has a shape of (3 x 3) -ie (inputs.shape[0] x (weights.T).shape[1]). 

This means that the each weight set for the weights for the second layer must have a shape[1] of 3. Put another way, 
since the number of rows from layer1_output is 3, the number of columns in the weights for the second layer must be 3
for matrix multiplication to be satisfied. We can have as many rows as we want for the weights (weights.shape[0]), 
this determines the number of neurons in the second layer. But each neuron must have 3 weight values.
in this case.
"""
weights2 = [[0.1, -0.14, 0.5],
            [-0.5, 0.12, -0.33],
            [-0.44, 0.73, -0.13], 
            [-0.31, -0.2, 0.55]]
biases2 = [-1, 2, -0.5, 0.2]

layer2_output = np.dot(layer1_output, np.array(weights2).T) + biases2
print(layer2_output)

"""
The second layer has 4 neurons. So the output has the shape (3 x 4). A third layer would
expect the weights to have a shape of (batch, 4). 
"""

weights3 = [[0.1, 0.2, 0.3, 0.4], 
            [0.5, -0.6, 0.7, -0.8],
            [-0.9, 0.1, 0.2, 0.3]]
biases3 = [1, 0.5, -0.1]

layer3_output = np.dot(layer2_output, np.array(weights3).T) + biases3
print(layer3_output)