# Backpropagation
Train a neural network through calculating the **error contribution** of each perceptron - adjusting the weights of perceptrons.

## Basic Algorithm
1. Complete a feedforward operation
2. Compare output of model with desired output
3. Calculate error
4. Run feedforward operation backwards (backpropagation) to **spread the error** to each of the weights
5. Update the weights and get a better model
6. Repeat until good model is reached

## TODO: DERIVATION