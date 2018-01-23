# Local Minimum Problem
Training algorithms (gradient descent) unable to 'see' the global minimum and get 'stuck' in a local minimum.

Gradient descent will reach the local minimum and assume it is finished:

![](../../images/2018-01-23-07-38-35.png)

## Solution: Random Restart
Run gradient descent multiple times, each starting from a random point.
* Increases the *probability* of reaching the global minimum
* Or at least finding a local minimum which is a reasonable approximation of the global minimum.

![](../../images/2018-01-23-07-39-59.png)

![](../../images/2018-01-23-07-40-09.png)

## Solution: Momentum
Give the step size a momentum, in order to 'overcome' local minima.

Helps accelerate SGD in the relevant direction and dampens oscillations. 

Each step is the average of the previous steps, weighted by &beta; momentum constant in range (0,1) - often around **0.9**:
* step(n) &rarr; step(n) + &beta;step(n-1) + &beta;<sup>2</sup>step(n-2)+...
* &beta; term uses increasing powers to weight recent steps more heavily that past steps

1. v<sub>t</sub>=&beta;<sup>i+1</sup>v<sub>t-1</sub> + &alpha;&nabla;<sub>W</sub>E(W)
2. W = W-v<sub>t</sub>
    * v<sub>i</sub> = update vector at time *i*
    * &alpha; = learning rate
    * E(W) = Error function
    * W = Weights matrix(parameters)

![](../../images/2018-01-23-07-49-27.png)

## Nesterov Accelerated Gradient (NAG)
Extension of momentum that slows down as gradient begins to increase to smooth the ascent.
* momentum = ball rolling down a hill, following the slope blindly
* NAG = smarter ball, has notion of where it is going to it slows down before the hill slopes up again

NAG makes a jump in the direction of the previous accumulated gradient, then measures this new gradient and makes a **correction**.

1. v<sub>t</sub>=&beta;<sup>i+1</sup>v<sub>t-1</sub> + &alpha;&nabla;<sub>W</sub>E(W-&beta;<sup>i+1</sup>v<sub>t-1</sub>)
2. W = W-v<sub>t</sub>

![](../../images/2018-01-23-08-39-21.png)
*  Blue = Momentum
* Brown = first NAG jump
* Red = NAG correction
* Green = NAG complete update

Anticipatory update prevents moving too fast &rarr; increased responsiveness.

Updates adapt to the slope of the error function &rarr; speed up Gradient Descent.

See [Optimizers](./optimizers.md) notes for futher detail and solutions to gradient descent problems.