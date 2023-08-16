"""
Implementation of the PaLM model released by Google.

"""

import tensorflow as tf
from tensorflow import keras
from keras import layers, models
from einops import rearrange, repeat

# the residual & skip connections

class Residual(layers.Layer):
    def __init__(self, fn):
        super(Residual, self).__init__()
        self.fn = fn

    def __call__(self, x):
        return self.fn(x) + x
    

# RoPE embeddings -> Rotary Positional Embeddings
# einsum equation & docs -> https://www.tensorflow.org/api_docs/python/tf/einsum
def fixed_pos_embedding(x, seq_len):
    dim = x.shape[-1]
    inv_freq = 1.0 / (1000 ** (tf.range(0, dim, 2) / dim))

    seq = tf.range(seq_len)
    sinusoid_inp = tf.einsum('i, j -> i j', seq, inv_freq) # output[i, j] = seq[i] * inv_freq[j]

    return tf.concat([sinusoid_inp, sinusoid_inp], axis=-1)


def rotate_half(x):
    x1 = x[:, :, ::2]
    x2 = x[:, :, 1::2]

    x = tf.stack((-x2, x1), axis = -1)

    return rearrange(x, "... d j -> ... (d j)")


def apply_rotary_emb(pos, t):
    return (t * pos.cos()) + (rotate_half(t) * pos.sin())


class ParallelTransformerBlock(layers.Layer):
    def __init__(self, d_model, dim_head = 64, heads = 8, ff_mult = 4):
        super(ParallelTransformerBlock, self).__init__()
        
        self.heads = heads
        self.layer_norm = layers.LayerNormalization(epsilon=1e-6)



    def __call__(self, x):
        n, h = x.shape[1], self.heads

        # pre layer-norm
        x = self.layer_norm(x)



class PaLM(models.Model):
    def __init__(self, d_model, num_tokens, depth, heads, ff_mult):
        self.embedding_layer = layers.Embedding(num_tokens, d_model)


    def __call__(self, x):
        x = self.embedding_layer(x)
        x = 