"""This python code contains some operations with tensors implemented from scratch
"""
import numpy as np

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

def relu_3d(x):
    """An expansion of the ReLU activation for rank 3 tensors"""
    assert len(x.shape) == 3
    x = x.copy()

    x = x.astype(np.float32)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            for k in range(x.shape[2]):
                x[i, j, k] = max(x[i, j, k], 0)
    return x

def add_2d(x, y):
    """Element-wise addition operation of two arrays.
    Expects x and y to be rank-2 numpy tensors

    In numpy, would simply be z = x + y
    """
    assert len(x.shape) == 2
    assert x.shape == y.shape # x and y need to be sampe shape

    x = x.copy()
    x = x.astype(np.float32)
    y = y.astype(np.float32)
    
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[i, j]
    return x


def add_3d(x, y):
    """Element-wise addition operation of a rank-3 tensor"""
    assert len(x.shape) == 3
    assert x.shape == y.shape

    x = x.copy()
    x = x.astype(np.float32)
    y = y.astype(np.float32)

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            for k in range(x.shape[2]):
                x[i, j, k] += y[i, j, k]
    return x

def add_matrix_vector(x, y):
    """Element-wise addition of a matrix to a vector.
    The add functions above require both x and y to be of the same shape. 
    x.shape - (a, b)
    y.shape - (a,)
    This function requires broadcasting.
    """
    assert len(x.shape) == 2 # assert that x is a matrix (2D array)
    assert len(y.shape) == 1 # assert that y is a vector (1D array)

    x = x.copy()
    x = x.astype(np.float32)
    y = y.astype(np.float32)

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[j]
    return x

def vector_dot(x, y):
    """Implementation of the vector dot product.
    
    Requires x and y to be vectors.
    In numpy, would be z = np.dot(x, y)
    vector dot product returns a scalar
    """
    assert len(x.shape) == 1
    assert len(y.shape) == 1
    x = x.astype(np.float32)
    y = y.astype(np.float32)

    z = 0
    for i in range(x.shape[0]):
        z += x[i] * y[i]
    return z

def matrix_vector_dot(x, y):
    """Implementation of dot product for a matrix and a scalar

    Returns a vector of the dim 0 of x (rows)
    """
    assert len(x.shape) == 2
    assert len(y.shape) == 1
    assert x.shape[1] == y.shape[0] # number of columns of first = rows of vector
    x = x.astype(np.float32)
    y = y.astype(np.float32)

    z = np.zeros(x.shape[0])

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            z[i] += x[i, j] * y[j]
    return z

def cross_product(x, y):
    """Implementation of the cross product of two rank-2 arrays
    
    Requires the x.shape[1] (columns) to equal y.shape[0]
    
    Returns a rank-2 array of shape (x.shape[0], y.shape[1])
    """
    assert len(x.shape) == 2
    assert len(y.shape) == 2
    assert x.shape[1] == y.shape[0]
    x = x.astype(np.float32)
    y = y.astype(np.float32)

    z = np.zeros((x.shape[0], y.shape[1]))

    for i in range(x.shape[1]):
        for j in range(y.shape[0]):
            row_x = x[i, :]
            column_y = y[:, j]
            z[i, j] = vector_dot(row_x, column_y)
    return z



if __name__ == '__main__':
    x = [[1, 2, -3, 4], [1, 0, 0, 4]]
    x = np.array(x)

    y = relu_2d(x)
    print(y)

    z = add_2d(x, y)
    print(z)

    d = np.expand_dims(x, axis=0)
    e = relu_3d(d)
    print(e)

    a = [1, 2, 3, 5]
    a = np.array(a)

    b = add_matrix_vector(z, a)
    print(b)

    c = vector_dot(a, a)
    print(c)

    d = matrix_vector_dot(x, a)
    print(d)

    x = [[1, 2], [1, 4]]
    y = [[2, 4], [6, 4]]
    x = np.array(x)
    y = np.array(y)
    e = cross_product(x, y)
    print(e)