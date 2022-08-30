"""
Author: Akorede Adewole, 2022.

Implementation of a simple training loop with TensorFlow.
File is simply to understand how a TensorFlow training loop looks for other tasks
"""
import tensorflow as tf


# necessary parameters for training loop
model = ""
optimizer = ""
learning_rate = 0.1
epochs = 2


# sample loss
def square_loss(true, pred):
    sample_loss = tf.square(pred - true)
    return tf.reduce_mean(sample_loss)

def training_step(inp, tar):
    # for each epoch
    for epoch in range(epochs):
        # iterate the dataset
        for step, (inp, train) in enumerate(train):
            with tf.GradientTape() as tape: # open the gradient tape for auto-differentiation
                pred = model(inp)
                loss = square_loss(tar, pred)
            grads = tape.gradient(loss, model.trainable_parameters)
            optimizer.apply_gradients(zip(grads, model.trainable_weights))

            print("LOGS")