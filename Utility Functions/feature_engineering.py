import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

train = "A dataframe"
# for Gender
ohe = OneHotEncoder()
ohe.fit(train[['Gender']])
temp = ohe.transform(train[['Gender']]).toarray()
temp = pd.DataFrame(temp, columns=ohe.get_feature_names_out())
train = pd.concat([train, temp], axis=1).drop(columns=['Gender'])

# OHE of labels for Deep Learning Tensors
def to_one_hot(labels, dimension=46):
    """Does the same thing as Keras's to_categorical() function.
    
    Labels are the vectors to OHE
    Dimension refers to the number of classes for labels
    """
    results = np.zeros((len(labels), dimension))

    for i, label in enumerate(labels):
        results[i, label] = 1.
    return results