import numpy as np

class Loss:
    def calculate(self, output, y):
        # calculate the data_loss and regularization loss given data input and desired output
        sample_losses = self.forward(output, y)
        loss = np.mean(sample_losses)
        return loss

class CategoricalCrossEntropy(Loss):
    """This class is for when the target is one-hot encoded"""
    def forward(self, y_pred, y_true):
        # y_pred is the output of the neural network, y_true is the true label
        # y_pred is a numpy array of shape (n_examples, n_outputs)
        # y_true is a numpy array of shape (n_examples, n_outputs)
        # return the cross entropy loss
        
        samples = len(y_pred)
        # clip data to prevent division by 0
        # upper & lower to avoid mean tending toward any value
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7) 

        assert len(y_true.shape) == 2 # 2D array
        correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)
        neg_log = -np.log(correct_confidences)
        return neg_log


class SparseCategoricalCrossEntropy(Loss):
    """This class is implemented for when the target is not one-hot encoded"""
    def forward(self, y_pred, y_true):
        # y_pred is the output of the neural network, y_true is the true label
        # y_pred is a numpy array of shape (n_examples, n_outputs)
        # y_true is a numpy array of shape (n_examples, n_outputs)
        # return the cross entropy loss
        samples = len(y_pred)
        # clip data to prevent division by 0
        # upper & lower to avoid mean tending toward any value
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7) 

        assert len(y_true.shape) == 1

        correct_confidences = y_pred_clipped[range(samples), y_true]
        neg_log = -np.log(correct_confidences)
        return neg_log