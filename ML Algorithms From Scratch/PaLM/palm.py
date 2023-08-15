"""
Implementation of the PaLM model released by Google.

"""

import tensorflow as tf
from tensorflow import keras
from keras import layers, models

# the residual & skip connections

class Residual(layers.Layer):
    def __init__(self, fn):
        super(Residual, self).__init__()
        self.fn = fn

    def __call__(self, x):
        return self.fn(x) + x
    

# swiglu activation
