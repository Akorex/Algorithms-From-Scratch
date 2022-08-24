import numpy as np

def accuracy(pred, true):
    """Returns the accuracy score.
    
    pred - the output of the Dense layer with softmax activation -- 2D array
    true - class targets. could be 1D or 2D arrays
    """
    predictions = np.argmax(pred, axis=1)
    
    if len(true.shape) == 2:
        true = np.argmax(true, axis=1)
    
    accuracy = np.mean(predictions == true)
    return accuracy

if __name__ == '__main__':
    y_hat = np.array([[0.7, 0.2, 0.1], 
                    [0.5, 0.1, 0.4], 
                    [0.02, 0.9, 0.8]])
    
    y = np.array([[1, 0, 0], 
                [0, 1, 0], 
                [0, 1, 0]])

    acc = accuracy(y_hat, y)
    print(acc)