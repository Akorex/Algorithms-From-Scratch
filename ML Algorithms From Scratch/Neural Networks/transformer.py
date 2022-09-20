# implement the encoder layer in TensorFlow

class Encoder(tf.keras.layers.Layer):
    def __init__(self, N, d_model, num_heads, dff, rate=0.1):
        super(Encoder, self).__init__()

        self.mha = [MultiHeadAttention(d_model, num_heads) for _ in range(N)]
        self.ffn = [FeedForward(d_model, dff) for _ in range(N)]

        self.layer_norm = [LayerNormalization() for _ in range(N)]
        self.dropout1 = [Dropout(rate) for _ in range(N)]
        self.dropout2 = [Dropout(rate) for _ in range(N)]

    def call(self, x, training, mask):
        for i in range(len(self.mha)):
            x = self.mha[i](x, x, x, mask)
            x = self.dropout1[i](x, training=training)
            x = self.layer_norm[i](x + x)
            x = self.ffn[i](x)
            x = self.dropout2[i](x, training=training)
        return x

# implement MultiHeadAttention in TensorFlow
class MultiHeadAttention(tf.keras.layers.Layer):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()

        self.num_heads = num_heads
        self.d_model = d_model

        assert d_model % self.num_heads == 0

        self.depth = d_model // self.num_heads

        self.wq = tf.keras.layers.Dense(d_model)
        self.wk = tf.keras.layers.Dense(d_model)
        self.wv = tf.keras.layers.Dense(d_model)

        self.dense = tf.keras.layers.Dense(d_model)

    def split_heads(self, x, batch_size):
        x = tf.reshape(x, (batch_size, -1, self.num_heads, self.depth))
        return tf.transpose(x, perm=[0, 2, 1, 3])

    def call(self, q, k, v, mask):
        batch_size = tf.shape(q)[0]

        q = self.wq(q)
        k = self.wk(k)
        v = self.wv(v)

        q = self.split_heads(q, batch_size)
        k = self.split_heads(k, batch_size)
        v = self.split_heads(v, batch_size)

        scaled_attention, attention_weights = scaled_dot_product_attention(q, k, v, mask)

        scaled_attention = tf.transpose(scaled_attention, perm=[0, 2, 1, 3])

        concat_attention = tf.reshape(scaled_attention, (batch_size, -1, self.d_model))

        output = self.dense(concat_attention)
        
        return output, attention_weights