# Mini-Batching
Technique for training on subsets of a dataset instead of all the data at one time.
* Allows training of a model when computer has **insufficient memory** to store the entire dataset
* Computationally inefficient -> can't calcluate loss simultaneously across all samples
    * Still better than not being able to train the model at all
* Works well with Stochastic Gradient Descent
    * Randomly shuffle data at start of each epoch
    * Create mini batches
    * Train network with Gradient Descent on each mini batch
    * Batches are random -> Stochastic Gradient Descent

## Small Dataset -> No Mini Batching
```Python
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

n_input = 784  # MNIST data input (img shape: 28*28)
n_classes = 10  # MNIST total classes (0-9 digits)

# Import MNIST data
mnist = input_data.read_data_sets('/datasets/ud730/mnist', one_hot=True)

# The features are already scaled and the data is shuffled
train_features = mnist.train.images # Shape (55000, 784) Type: float32
test_features = mnist.test.images 

train_labels = mnist.train.labels.astype(np.float32) # Shape (55000, 10) Type: float32
test_labels = mnist.test.labels.astype(np.float32)

# Weights & bias
weights = tf.Variable(tf.random_normal([n_input, n_classes])) # Shape (784, 784) Type: float32
bias = tf.Variable(tf.random_normal([n_classes])) # Shape (10,) Type: float32
``` 
### Memory Sizes
* `float32` = 32 bits
* `train_features = 55000*784*32` = 1379840000 bits = **172480000 bytes**
* `train_labels = 55000*10*32` = 17600000 bits = **2200000 bytes**
* `weights = 784*10*32` = 250880 bits = **31360 bytes**
* `bias = 10*32` = 320 bits = **40 bytes**
* Total = **174 megabytes**

* This dataset is small enough to train on most CPU's and GPU's
* Larger datasets will measure in **Gigabytes or more**

## TensorFlow Mini-Batching
* Divide data into batches
* Can't always be equal sizes
    * 1000 samples, batch size of 128:
        * `1000 // 128 = 7` -> 7 batches of 128
        * `1000 % 128 = 104` -> 1 batch of 104
* Size of batches can vary
    * Use `tf.placeholder()`
    ```Python
    n_input = 784 # Number of features in each sample
    n_classes = 10 # Possible labels

    # Features and Labels
    features = tf.placeholder(tf.float32, [None, n_input])
    labels = tf.placeholder(tf.float32, [None, n_classes])
    # None dimension is a placeholder for the batch size. At runtime, TensorFlow will accept any batch size greater than 0
    ```
```Python
from pprint import pprint

def batches(batch_size, features, labels):
    """
    Create batches of features and labels
    :param batch_size: The batch size
    :param features: List of features
    :param labels: List of labels
    :return: Batches of (Features, Labels)
    """
    assert len(features) == len(labels)
    # TODO: Implement batching
    batches = []
    for i in range(0, len(features), batch_size):
        batches.append((features[i:i+batch_size], labels[i:i+batch_size]))
    return batches

# 4 Samples of features
example_features = [
    ['F11','F12','F13','F14'],
    ['F21','F22','F23','F24'],
    ['F31','F32','F33','F34'],
    ['F41','F42','F43','F44']]
# 4 Samples of labels
example_labels = [
    ['L11','L12'],
    ['L21','L22'],
    ['L31','L32'],
    ['L41','L42']]

pprint(batches(3, example_features, example_labels))
# Output:
# [([['F11', 'F12', 'F13', 'F14'],
#    ['F21', 'F22', 'F23', 'F24'],
#    ['F31', 'F32', 'F33', 'F34']],
#   [['L11', 'L12'], ['L21', 'L22'], ['L31', 'L32']]),
#  ([['F41', 'F42', 'F43', 'F44']], [['L41', 'L42']])]
```

### TensorFlow MNIST Example
```Python
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
from helper import batches # From Mini-Batching previous code example

learning_rate = 0.001
n_input = 784  # MNIST data input (img shape: 28*28)
n_classes = 10  # MNIST total classes (0-9 digits)

# Import MNIST data
mnist = input_data.read_data_sets('/datasets/ud730/mnist', one_hot=True)

# The features are already scaled and the data is shuffled
train_features = mnist.train.images
test_features = mnist.test.images

train_labels = mnist.train.labels.astype(np.float32)
test_labels = mnist.test.labels.astype(np.float32)

# Features and Labels
features = tf.placeholder(tf.float32, [None, n_input])
labels = tf.placeholder(tf.float32, [None, n_classes])

# Weights & bias
weights = tf.Variable(tf.random_normal([n_input, n_classes]))
bias = tf.Variable(tf.random_normal([n_classes]))

# Logits - xW + b
logits = tf.add(tf.matmul(features, weights), bias)

# Define loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=labels))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

# Calculate accuracy
correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

batch_size = 128
assert batch_size is not None, 'You must set the batch size'

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    
    # Train optimizer on all batches
    for batch_features, batch_labels in batches(batch_size, train_features, train_labels):
        sess.run(optimizer, feed_dict={features: batch_features, labels: batch_labels})

    # Calculate accuracy for test dataset
    test_accuracy = sess.run(
        accuracy,
        feed_dict={features: test_features, labels: test_labels})

print('Test Accuracy: {}'.format(test_accuracy))
# Accuracy will be low -> only 1 epoch being used
```
