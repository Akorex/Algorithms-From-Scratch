import tensorflow as tf

# 1
x = tf.Variable(0.)
with tf.GradientTape() as tape:
    y = 2*x + 3

grad_of_y_wrt_x = tape.gradient(y, x)
print(grad_of_y_wrt_x)

# 2
W = tf.Variable(tf.random.uniform((2, 2)))
b = tf.Variable(tf.zeros((2,)))
x = tf.random.uniform((2, 2))

with tf.GradientTape() as tape:
    y = tf.matmul(x, W) + b

grad_of_y_wrt_W_and_b = tape.gradient(y, [W, b])
print(grad_of_y_wrt_W_and_b)

# 3
input_var = tf.Variable(initial_value=3.)
with tf.GradientTape() as tape:
    results = tf.square(input_var)

gradient = tape.gradient(results, input_var)
print(gradient)

# 4 - compute second-order gradients
time = tf.Variable(0.)
with tf.GradientTape() as tape:
    with tf.GradientTape() as inner_tape:
        position = 4.9 * time **2
    speed = inner_tape.gradient(position, time)
acceleration = tape.gradient(speed, time)

print(f"Speed: {speed}, Acceleration: {acceleration}")