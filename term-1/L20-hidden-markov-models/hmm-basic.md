# Hidden Markov Model Basics
Markov Model in which the **states are not observed**

Measurement variables (observations/evidence) are observed, from which **state can be inferred**

![](../images/2017-12-04-16-23-01.png)

![](../images/2017-12-04-16-21-45.png)

## Basic Inference
For HMM with parameters:
* Next state distribution
* Observation/measurement distribution
* Initial state distribution

Probability of a state X<sub>i</sub>, given an observation Z<sub>i</sub>:
* P(X<sub>i</sub>|Z<sub>i</sub>) = P(Z<sub>i</sub>|X<sub>i</sub>)&middot;P(X<sub>i</sub>) / P(Z<sub>i</sub>)
* Or with a normalizer: &alpha;P(Z<sub>i</sub>|X<sub>i</sub>)&middot;P(X<sub>i</sub>) 

Predict distribution of a state X<sub>i+1</sub>, given knowledge of X<sub>i</sub>:
* P(X<sub>i+1</sub>)=&sum;<sub>x<sub>i</sub></sub>P(X<sub>i</sub>)&middot;P(X<sub>i+1</sub>|X<sub>i</sub>)