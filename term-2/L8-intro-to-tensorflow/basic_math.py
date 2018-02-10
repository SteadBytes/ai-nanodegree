# Solution is available in the other "solution.py" tab
import tensorflow as tf

# Convert normal_math() to TensorFlow


def normal_math():
    x = 10
    y = 2
    z = x/y - 1
    return z


def tf_math():
    x = tf.constant(10)
    y = tf.constant(2)
    z = tf.subtract(tf.divide(x, y), tf.cast(tf.constant(1), tf.float64))

    with tf.Session() as sess:
        output = sess.run(z)
    return output
