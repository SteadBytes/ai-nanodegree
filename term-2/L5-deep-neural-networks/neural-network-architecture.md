# Neural Network Architecture
Multi-layer combinations of linear perceptron models.

![](../../images/2018-01-18-12-28-09.png)

## Non-Linear Models
Combine linear regions to produce non-linear regions:

![](../../images/2018-01-18-12-16-34.png)

Linear model = linear probability space:
* Gives classificiation probability of each point in the space (probability of each point being blue in example)

Combine the probabilities of each point:
* Add the probabilities -> apply sigmoid function
    * Sum of probabilities > 1, sigmoid outputs between 0-1

![](../../images/2018-01-18-12-19-59.png)

With weights and bias:

![](../../images/2018-01-18-12-20-28.png)

### Using Perceptrons
Combine perceptrons of linear models by passing outputs into another perceptron with model weights/bias:

![](../../images/2018-01-18-12-22-52.png)

Combine using linear equation 7&middot;Model<sub>1</sub> + 5&middot;Model<sub>2</sub> -6:

![](../../images/2018-01-18-12-25-15.png)

Removing duplicate nodes:

![](../../images/2018-01-18-12-25-58.png)

## Multiple Layers
Create complex neural networks by changing the architecture:
* Add more nodes to input, hidden and output layer
    * n-nodes in input layer = output data in n-dimensional space


![](../../images/2018-01-18-12-29-57.png)

![](../../images/2018-01-18-12-30-09.png)

* Add more layers -> **deep neural network**
    * Linear models combine to create non-linear models, which then combine to create even more non-linear models
    * Repeat to create highly complex models with many hidden layers

![](../../images/2018-01-18-12-31-39.png)

![](../../images/2018-01-18-12-32-52.png)

## Multi-Class Classification
Each node in the output layer represents a class and gives the probability of the input being that class. Use **Softmax** on the outputs to obtain well-defined probabilities for each class.
* Number of nodes in output layer = number of classes

Classifying an image into Duck, Beaver or Walrus:

![](../../images/2018-01-18-12-35-15.png)