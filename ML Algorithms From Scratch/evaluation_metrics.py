"""
Author: Akorede Adewole, 2022.
This file contains implementation of ML metrics for classification and regression from scratch
The metrics are useful for metrics encountered with Tabular data.

These implementations are for academic purposes only.
"""
import numpy as np

#--------------- classification metrics -------------------------
def accuracy(y_true, y_pred):
    """Returns the ratio of correctly classified classes to number of classes overall
    Args:
          needs len(y_true) to be equal to len(y_pred)
          y_true: list of true values
          y_pred: list of predicted values
    """
    counter = 0 # keeps a count of correct predictions
    if len(y_true) != len(y_pred):
        raise ValueError('length of the classes need to match')
    for yt, yp in zip(y_true, y_pred):
        if yt == yp:
            counter += 1
        
    return counter/ len(y_true)

def true_positive(y_true, y_pred):
    """Returns the count of true positives
    Args:
          expecting binary values of 0 and 1
          needs len(y_true) to be equal to len(y_pred)
          y_true: list of true values
          y_pred: list of predicted values
    """
    tp = 0 # to count the true positives
    for yt, yp in zip(y_true, y_pred):
        if yt == 1 and yp == 1:
            tp += 1

    return tp

def true_negative(y_true, y_pred):
    """Returns the count of true negatives
    Args: 
        expecting binary values of 0 and 1
        needs len(y_true) to be equal to len(y_pred)
        y_true: list of true values
        y_pred: list of predicted values
    """
    tn = 0 # a count of true negatives
    for yt, yp in zip(y_true, y_pred):
        if yt == 0 and yp == 0:
            tn += 1

    return tn

def false_positive(y_true, y_pred):
    """Returns the count of classes incorrectly classified as positive
    Args: 
         expecting binary values of 0 and 1
         needs len(y_true) to be equal to len(y_pred)
         y_true: list of true values
         y_pred: list of predicted values
    """
    fp = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 0 and yp == 1:
            fp += 1
    return fp

def false_negative(y_true, y_pred):
    """Returns the count of classes incorrectly classified as negative
    Args: 
         expecting binary values of 0 and 1
         needs the two lists to be of equal length
         y_true: list of true values
         y_pred: list of predicted values
    """
    fn = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 1 and yp == 0:
            fn += 1
    return fn

def precision_score(y_true, y_pred):
    """Returns the precision score
    Precision is defined as TP/(TP + FP)"""
    tp = true_positive(y_true, y_pred)
    fp = false_positive(y_true, y_pred)

    return tp / (tp + fp)

def recall_score(y_true, y_pred):
    """Returns the recall score
    Recall is defined is the ratio of positive instances correctly classified
    Also known as True Positive Rate or Sensitivity
    Defined as: TP/ (TP + FN)
    """
    tp = true_positive(y_true, y_pred)
    fn = false_negative(y_true, y_pred)

    return tp / (tp + fn)

def f1_score(y_true, y_pred):
    """Returns the F1 score.
    F1 is the harmonic mean of recall and precision with each having equal weights
    Defined as: 2PR/(P + R)
    """
    p = precision_score(y_true, y_pred)
    r = recall_score(y_true, y_pred)
    score = (2*p*r)/(p + r)

    return score

def false_positive_rate(y_true, y_pred):
    """Returns the false positive rate, FPR = FP / (FP + TN)"""
    fp = false_positive(y_true, y_pred)
    tn = true_negative(y_true, y_pred)

    score = fp /(fp + tn)
    return score

def specificity(y_true, y_pred):
    """returns the specificity. defined as 1 - FPR
    Also known as True Negative Rate"""
    fpr = false_positive_rate(y_true, y_pred)
    score = 1 - fpr

    return score

def log_loss(y_true, y_proba):
    """
    Function to calculate log loss
    Args: 
         y_true - list of true values
         y_proba - list of probabilities for 1
    """
    epsilon = 1e-15
    loss = []

    for yt, yp in zip(y_true, y_proba):
        yp = np.clip(yp, epsilon, 1- epsilon)
        temp_loss = -1.0 * (yt * np.log(yp)) + (1 - yt) * (np.log(yp))
        loss.append(temp_loss)
    return np.mean(loss)

# ---------- regression metrics -----------------------------------
if __name__ == '__main__':
    l1 = [0,1,1,1,0,0,0,1]
    l2 = [0,1,0,1,0,1,0,0]
    print(accuracy(l1, l2))
    print(true_positive(l1, l2))
    print(true_negative(l1, l2))
    print(false_positive(l1, l2))
    print(false_negative(l1, l2))
    print(precision_score(l1, l2))
    print(recall_score(l1, l2))
    print(f1_score(l1, l2))