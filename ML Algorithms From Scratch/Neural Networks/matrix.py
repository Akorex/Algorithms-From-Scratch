import numpy as np
from tensor_operations import cross_product

A = [[1, 2, 3], 
    [6, 0, 3], 
    [1, 1, 7]]

B = [[2, 1, 1], 
    [6, 2, 6], 
    [0, 0, 1]]

A = np.array(A)
B = np.array(B)

print(cross_product(B, A))