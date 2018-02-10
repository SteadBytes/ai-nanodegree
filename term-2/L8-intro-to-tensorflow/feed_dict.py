import tensorflow as tf

# use tf.placeholder() to set input before a session runs
# can't just set a varable to the dataset as tensorflow models are designed
# to take different datasets and parameters

# Use `feed_dict` parameter in tf.session.run() to set the placeholder tensor


def run_123():
    # demonstrate feed_dict with 1 tensor to always return the value 123
    output = None
    x = tf.placeholder(tf.int32)

    with tf.Session() as sess:
        output = sess.run(x, feed_dict={x: 123})
    return output


def run_multiple():
    # demonstrate feed_dict with multiple tensors
    x = tf.placeholder(tf.string)
    y = tf.placeholder(tf.int32)
    z = tf.placeholder(tf.float32)

    with tf.Session() as sess:
        output = sess.run(x, feed_dict={x: 'Test String', y: 123, z: 45.67})
    return output
