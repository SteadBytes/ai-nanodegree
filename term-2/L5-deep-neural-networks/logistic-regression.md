# Logistic Regression
Minimize the error function of a model, given training data:
* Pick a random model
* Calculate error
* Minimize error to obtain a better model
    * Gradient descent
* Repeat

## For model using &sigma;(Wx+b) Activation Function
1. Start with random weights and bias:
    * w<sub>1</sub>,...,w<sub>n</sub>,b
2. For every point (w<sub>x</sub>,...,x<sub>n</sub>):
    * For i=1...n:
        * Update w'<sub>i</sub> = w<sub>i</sub> + &alpha;(y-y&#770;)x<sub>i</sub>
        * Update b' = b + &alpha;(y-y&#770;)x<sub>i</sub>

```Python
import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x)*(1-sigmoid(x))

def prediction(X, W, b):
    return sigmoid(np.matmul(X,W)+b)

def error_vector(y, y_hat):
    return [-y[i]*np.log(y_hat[i]) - (1-y[i])*np.log(1-y_hat[i]) for i in range(len(y))]

def error(y, y_hat):
    ev = error_vector(y, y_hat)
    return sum(ev)/len(ev)

def dErrors(X, y, y_hat):
    """ Calculate gradient of the error function
    Args:
        X (list of lists): List of inputs [[x1, x2], [x1,x2]...]
        y (list): List of expected outputs for each input (same order) i.e. expected output for X[0] = y[0]
        y_hat (list): List of predections for each input (same order)
        i.e. prediction for X[0] = y[0]
    Returns:
        3-tuple of lists:
            Gradients of X w.r.t w1
            Gradients of X w.r.t w2
            Gradients of X w.r.t b
    """
    DErrorsDx1 = [-X[i][0]*(y[i]-y_hat[i]) for i in range(len(y))]
    DErrorsDx2 = [-X[i][1]*(y[i]-y_hat[i]) for i in range(len(y))]
    DErrorsDb = [-(y[i]-y_hat[i]) for i in range(len(y))]
    return DErrorsDx1, DErrorsDx2, DErrorsDb

def gradientDescentStep(X, y, W, b, learn_rate = 0.01):
    """ Performs a gradient descent iteration/step, updating weights and bias.
    Args:
        X (list of lists): List of inputs [[x1, x2], [x1,x2]...]
        y (list): List of expected outputs for each input (same order) i.e. expected output for X[0] = y[0]
        W (list): List of weights [w1,w2]
        b (int or float): bias
        learn_rate (int): Learning rate constant factor applied to adjustments
    Returns:
        3-tuple:
            Updated weights: W
            Updated bias: b
            Error of current model
    """
    # Calculate the prediction
    y_hat = prediction(X, W, b)
    #Calculate the gradient
    Dx1, Dx2, Db = dErrors(X, y, y_hat)
    #Update the weights and bias
    W[0] -= sum(Dx1)*learn_rate
    W[1] -= sum(Dx2)*learn_rate
    b -= sum(Db)*learn_rate
    # This calculates the error
    e = error(y, y_hat)
    return W, b, e

def trainLogisticRegression(X, y, learn_rate = 0.01, num_epochs = 100):
    """ Repeatedly runs the gradient descent algorihtm on the dataset 
    Args:
        X (list of lists): List of inputs [[x1, x2], [x1,x2]...]
        y (list): List of expected outputs for each input (same order) i.e. expected output for X[0] = y[0]
        learn_rate (int): Learning rate constant factor applied to adjustments
        num_epochs (int): Number of iterations to run gradient descent
    Returns:
        2-tuple:
            list of lines (tuples) representing adjusted boundary lines at each epoch
            list of points representing error at each epoch
    """
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    # Initialize the weights randomly
    W = np.array(np.random.rand(2,1))*2 -1
    b = np.random.rand(1)[0]*2 - 1
    # Lines for plotting visualisations
    boundary_lines = []
    errors = []
    for i in range(num_epochs):
        # In each epoch, apply the gradient descent step.
        W, b, error = gradientDescentStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
        errors.append(error)
    return boundary_lines, errors
```