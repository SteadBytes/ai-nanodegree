import tensorflow as tf

# create new TensorFlow object
hello_constant = tf.constant('Hello World!')

with tf.Session() as sess:
    # run tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)
