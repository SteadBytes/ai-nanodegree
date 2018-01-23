# Gradient Descent Optimization

## Challenges
* Choosing learning rate
    * Too small = slow convergence
    * Too big = hinder convergence
* Learning rate schedules
    * Adjust learning rate during training
        * According to pre-defined schedule
        * Threshold of change in objective between epochs
    * Must be defined in advance
        * Cannot adapt to characteristics of data set
* Adjusting learning rate for different parameters
    * Sparse data &rarr; some features have very different frequencies
        * Use larger learning rate for rare features
* Local minima
    * See [local-minimum](./local-minimum.md) for basics

## Adagrad
Gradient-based optimization algorithm that **adapts the learning rate *to* the parameters**.
* Infrequent parameters = larger updates
* Frequent parameters = smaller updates

Good for **sparse data**

Uses a different learning rate  at each time step *t* for **every parameter** W<sub>i</sub> based on **past gradients for W<sub>i</sub>**

Eliminates need to manually tune learning rate &alpha;
* Often just use a default value of 0.01

W<sub>t+1</sub> = W<sub>t</sub> - (&alpha;/sqrt(G<sub>t</sub>+&epsilon;))&#8857; g<sub>t</sub>
* G<sub>t</sub> &isin; R<sup>dxd</sup> = diagonal matrix, where each diagonal element i,i = sum of the squares of the gradients w.r.t W<sub>i</sub> up to time step *t*
* &epsilon; = smoothing term (avoid division by 0, often 1e-8)
* g<sub>t</sub> = Matrix of gradients of objective/error function w.r.t each parameter W<sub>i</sub> at time step *t*
* &#8857; = element-wise matrix-vector multiplication

**Weakness** = accumulation of squared gradients in denominator keeps growing during training.
* Learning rate shrinks - becoming infinitely small
    * Learning stops -> can't acquire additional knowledge

### Derivation
* Gradient of objective/error function w.r.t parameter W<sub>i</sub> at time step *t*:
    * g<sub>t,i</sub> = &nabla;<sub>W</sub>E(W<sub>t,i</sub>)
* SGD update for each parameter W<sub>i</sub>:
    * W<sub>t+1,i</sub> = W<sub>t,i</sub> - &alpha;&middot;g<sub>t,i</sub>
* Adagrad update rule - modifies &alpha; for each W<sub>i</sub> based on it's past gradients:
    * W<sub>t+1,i</sub> = W<sub>t,i</sub> - (&alpha;/sqrt(G<sub>t,ii</sub>+&epsilon;))&#8857; g<sub>t,i</sub>
    * G<sub>t</sub> &isin; R<sup>dxd</sup> = diagonal matrix, where each diagonal element i,i = sum of the squares of the gradients w.r.t W<sub>i</sub> up to time step *t*
    * &epsilon; = smoothing term (avoid division by 0, often 1e-8)
* G<sub>t</sub> contains sum of squares of past gradients w.r.t all parameters W along its diagonal &rarr; can **vectorize** using lement-wise matrix-vector multiplication - &#8857; between G<sub>t</sub> and g<sub>t</sub>:
    * W<sub>t+1</sub> = W<sub>t</sub> - (&alpha;/sqrt(G<sub>t</sub>+&epsilon;))&#8857; g<sub>t</sub>