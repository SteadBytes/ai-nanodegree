# Probability Distributions

**Probability Density Function**:
* Probability that random variable X falls into an interval around *x* divided by the width of the interval, as the interval width goes to zero
* P(x)=lim<sub>dx&rarr;0</sub>P(x<=X<=x+dx)/dx
* Must be nonnegative for all *x*
* Must have &int;<sub>-&infin;</sub><sup>&infin;</sup>P(x)dx=1

**Cumulative Probability Density Function**:
* Probability of a random variable being less than x
* F<sub>X</sub>(x)=P(X<=x)=&int;<sub>-&infin;</sub><sup>x</sup>P(u)du

**Gaussian/Normal Distribution**
* P(x) = (1/&sigma;&middot;sqrt(2&pi;))&middot;*e*<sup>-(x-&mu;)<sup>2</sup>/(2&sigma;<sup>2</sup>)</sup>
    * &mu; = mean
    * &sigma; = standard deviation
    * x = continous variable -&infin;<=x<=&infin;
* Standard Normal Distribution:
    * Normal distribution with &mu;=0 and variance &sigma;<sup>2</sup>=1

**Multivariate Gaussian Distribution**:
* Distribution over a vector **x** in *n* dimensions
* P(**x**) = (1/sqrt((2&pi;)<sup>n</sup>|**&Sigma;**|))&middot;*e*<sup>-1/2((**x**-**&mu;**)<sup>T</sup>**&Sigma;**<sup>-1</sup>(**x**-**&mu;**))
* **&mu;** = mean vector
* **&Sigma;** = covariance matrix

**Central Limit Theorem**:
* The distribution formed by sampling *n* independent random variables and taking their means tends to a normal distribution as *n* tends to infinity.

**Expectation**:
* Mean or average value for a random variable, weighted by the probability of each value
* Discrete variable: 
    * E(X) = &sum;<sub>i</sub>x<sub>i</sub>P(X=x<sub>i</sub>)
* Continuous variable:
    * E(X) = &int;<sub>-&infin;</sub><sup>&infin;</sup> xP(x)dx
    * Integral over probability density function P(x)

**Root Mean Square**:
* RMS of a set of values = square root of the mean of the squares of the values
* RMS(x<sub>1</sub>,...,x<sub>n</sub>)=sqrt((x<sub>1</sub><sup>2</sup>,...,x<sub>n</sub><sup>2</sup>)/n)

**Covariance**:
* Between two random variables = Expectation of the product of their differences from their means
* cov(X,Y)=E((X-&mu;x)(Y-&mu;y))

**Covariance Matrix**:
* Matrix of covariances between elements of a vector of random variables
* **&Sigma;**<sub>ij</sub>=cov(X<sub>i</sub>,X<sub>j</sub>)=E((X<sub>i</sub>-&mu;<sub>i</sub>)X<sub>j</sub>-&mu;<sub>j</sub>)
* **X** = <X<sub>1</sub>,...,X<sub>n</sub>><sup>T</sup>
* ![](../images/2017-12-05-13-55-15.png)