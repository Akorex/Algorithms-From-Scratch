import numpy as np


def smape(y_pred, y_true):
    """SMAPE refers to Symmetric mean absolute percentage error.
    
    returns the smape score
    """
    y_pred, y_true = np.array(y_pred), np.array(y_true)
    num =  np.sum(abs(y_pred - y_true))
    denom = np.sum(y_pred + y_true)
    smape = num/denom

    return smape


if __name__ == '__main__':
    y_pred = [20, 30, 40, 50]
    y_true = [20, 40, 50, 35]
    smape = smape(y_pred, y_true)
    print(smape)