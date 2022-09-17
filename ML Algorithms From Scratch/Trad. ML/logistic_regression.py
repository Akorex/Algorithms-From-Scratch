"""
Author: Akorede Adewole, 2022.

Implements Logistic Regression algorithm from scratch
"""
import numpy as np

np.random.seed(42)

class LogisticRegression:
    def __init__(self, epochs = 1000, lr = 1e-2):
        self.epochs = epochs
        self.lr = lr
        self.weights = None
        self.bias = None

    def _sigmoid(self, x):
        return 1./ (1 + np.exp(-x))

    def _prediction(self, features):
        """
        Computes the sigmoid activation function of the prediction by the logistic regression model.
        Values are between 0 and 1 - hence they are probabilities.
           Parameters
           ----------
        features : the independent variables or predictors
        """
        return self._sigmoid(np.dot(features, self.weights) + self.bias)
        

    def fit(self, X, y):
        """
        Fit the model according to the given training data.
        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Training vector, where n_samples is the number of samples and
            n_features is the number of features.
        y : array-like of shape (n_samples,)
            Target vector relative to X.

        Updates the weights and bias
        """
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.epochs):
            y_pred = self._prediction(X)
            error = y_pred - y.T
            error = np.reshape(error, n_samples)
            
            # calc gradients & update params
            dw = (1/ n_samples) * np.dot(X.T, error)
            db = (1/n_samples) * np.sum(error)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db
        
    def predict_proba(self, X):
        return self._prediction(X)

    def predict(self, X, threshold = 0.5):
        """
        Make predictions using the updated weight and bias.
        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Training vector, where n_samples is the number of samples and
            n_features is the number of features.
        default threshold = 0.5
       
        Returns
        -------
        Predictions 
        """
        predictions = np.array([1 if values >= threshold else 0 for values in self.predict_proba(X)])
        return predictions


if __name__ == '__main__':
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    import pandas as pd

    data = pd.read_csv(r'ML Algorithms From Scratch\Trad. ML\diabetes.csv')
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1:].values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    accuracy = accuracy_score(y_test, preds)
    print(accuracy)

    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    accuracy = accuracy_score(y_test, preds)
    print(accuracy)