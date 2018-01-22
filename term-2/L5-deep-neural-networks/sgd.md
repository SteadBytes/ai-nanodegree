# Stochastic Gradient Descent
A stochastic approximation of the gradient descent algorithm via iteration over subsets (batches) of training data.

## Motivation
Batch (normal) Gradient Descent uses **all the data points** in each epoch
* Large matrix computations = **computationally expensive**

## Iterative Method
Take small subsets (batches) of data, run each **in turn** through the neural network, calculate gradient of error function at those points and update weights in that direction. 

The true gradient of error function E(w) is approximated by a gradient at a single example (batch of data):
* w := w-&alpha;&nabla;E<sub>i</sub>(w)
    * w = parameter to be estimated (i.e. weights)
    * &alpha; = learning rate

Update above is run for each subset/batch of the training data set.
* If data split into 8 batches, 8 iterations will be run in order to use all the data in the training set.

