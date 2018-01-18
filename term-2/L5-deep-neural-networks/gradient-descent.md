# Gradient Descent
First-order iterative optimization algorithm for finding the **minimum of a function**. 

Takes steps proportional to the **negative of the gradient** of the function at the current point.
* Gradient *ascent* is the opposite

## General Definition
For a multivariable function **F(x)** that is *defined and differentiable* for a point *a*, **F(x)** decreases *fastest* moving from *a* in the direction of the negative gradient of **F** at *a* -&nabla;F(a):

If *a*<sub>n+1</sub> = *a*<sub>n</sub> - &gamma;&nabla;F(*a*<sub>n</sub>), for a *small enough* &gamma;
* F(*a*<sub>n</sub>) >= F(*a*<sub>n+1</sub>)
    * &gamma;&nabla;F(*a*<sub>n</sub>) is **subtracted** from *a* to move **against the gradient**

Start with *x*<sub>0</sub> as guess at local minimum of F:
* Sequence *x*<sub>0</sub>,*x*<sub>1</sub>/...*x*<sub>n</sub>   such that:
    * *x*<sub>n+1</sub> = *x*<sub>n</sub> - &gamma;<sub>n</sub>&nabla;F(*x*<sub>n</sub>), n>=0
* Then:
    * F(*x*<sub>0</sub>) >= F(*x*<sub>1</sub>) >= F(*x*<sub>2</sub>) >=...
* Sequence *x*<sub>n</sub> **converges to local minimum**

## Example for Error Function
For *m* points labelled x<sup>(1)</sup>,x<sup>(2)</sup>,...,x<sup>(m)</sup>:
* E = -1/m &sum;<sup>m</sup><sub>i=1</sub> (1-y<sub>i</sub>)(ln(1-y&#770;<sub>i</sub>)) + y<sub>i</sub>ln(&#770;<sub>i</sub>)
* Prediction y&#770;=&sigma;(Wx+b)

Goal: calculate gradient of E at a point x = (x<sub>1</sub>,...x<sub>n</sub>) given by **partial derivatives**:
* &nabla;E = &part;/&part;w<sub>1</sub> E,...,&part;/&part;w<sub>n</sub> E, &part;/&part;b E

Total error = average of errors at all points->calculate derivative of each point and average:
* Error produced by each point = E = −yln( y&#770;)−(1−y)ln(1− y&#770;)

### Sigmoid Derivative
&sigma;(x)=1/1+e<sup>x</sup>

* &sigma;'(x) = &part;/&part;x 1/1+e<sup>x</sup>
    * = ((&part;/&part;x 1 &middot; 1+e<sup>x</sup>) - (1&middot; &part;/&part;x 1+e<sup>-x</sup>)) / (1+e<sup>-x</sup>)<sup>2</sup>
        * Quotient rule
        * &part;/&part;x 1 e<sup>-x</sup> = &part;/&part;x 1 + &part;/&part;x e<sup>-x</sup>
        * = 0 + e<sup>-x</sup>&middot; &part;/&part;x -x
        * = -e<sup>-x</sup>
    * = ((1+e<sup>-x</sup>&middot;0) - (1&middot;-e<sup>-x</sup>)) / (1+e<sup>-x</sup>)<sup>2</sup>
    * = e<sup>-x</sup> / (1+e<sup>-x</sup>)<sup>2</sup>
    * = (1-1+e<sup>-x</sup>) / (1+e<sup>-x</sup>)<sup>2</sup>
    * = (1+e<sup>-x</sup> / (1+e<sup>-x</sup>)<sup>2</sup>) - 1 / (1+e<sup>-x</sup>)<sup>2</sup>
    * = (1 / (1+e<sup>-x</sup>))&middot;(1-1/(1+e<sup>-x</sup>))
    * = &sigma;(x)&middot;(1-&sigma;(x))

### Prediction y&#770; Derivative
y&#770; = &sigma;(Wx+b)

&part;/&part;w<sub>j</sub> y&#770; = y&#770;(1-y&#770;)&middot;x<sub>j</sub>

Derivation:
* &part;/&part;w<sub>j</sub> y&#770; = &part;/&part; w<sub>j</sub> &sigma;(Wx+b)
    * &sigma;(Wx+b)&middot;(1-&sigma;(Wx+b))&middot; &part;/&part;w<sub>j</sub>(Wx+b)
    * = y&#770;(1-y&#770;)&middot; &part;/&part;w<sub>j</sub>(Wx+b)
    * = y&#770;(1-y&#770;)&middot; &part;/&part; (w<sub>1</sub>x<sub>1</sub>+w<sub>2</sub>x<sub>2</sub>+...w<sub>n</sub>x<sub>n</sub> + b)
        * Only term in sum that is not constant w.r.t w<sub>j</sub> = w<sub>j</sub>x<sub>j</sub>
        * &part;/&part;w<sub>j</sub> w<sub>j</sub>x<sub>j</sub> = x<sub>j</sub>
    * = y&#770;(1-y&#770;)&middot;x<sub>j</sub>

### Error at point x Derivative w.r.t  weight w<sub>j</sub>
E = −yln( y&#770;)−(1−y)ln(1− y&#770;)

&part;/&part;w<sub>j</sub>E = -(y+y&#770;)&middot;x<sub>j</sub>

Derivation:
* &part;/&part;w<sub>j</sub>E = &part;/&part;w<sub>j</sub>[−yln( y&#770;)−(1−y)ln(1− y&#770;)]
    * =-y&part;/&part;w<sub>j</sub>log(y&#770;) - (1-y)&part;/&part;w<sub>j</sub>log(1-y&#770;)
    * = -y&middot;1/y&#770; &middot; &part;/&part;w<sub>j</sub>y&#770; - (1-y) &middot; log(1-y&#770;)
    * = -y&middot; 1/y&#770; &middot;y&#770;(1-y&#770;)&middot;x<sub>j</sub> - (1-y) &middot; &part;/&part;w<sub>j</sub> log(1-y&#770;)
        * &part;/&part;w<sub>j</sub>log(1-y&#770;) = 1/(1-y&#770;)&middot;&part;/&part;w<sub>j</sub>(1-y&#770;)
        * = 1/(1-y&#770;) &middot; -1 &middot; y&#770;(1-y&#770;)x<sub>j</sub>
    * = -y&middot; 1/y&#770; &middot;y&#770;(1-y&#770;)&middot;x<sub>j</sub> - (1-y) - (1-y)&middot; -1/(1-y&#770;) &middot; (-1)y&#770;(1-y&#770;)x<sub>j</sub>
    * = -y(1-y&#770;)x<sub>j</sub>-(1-y) -1 -1/(1-y&#770;)&middot;y&#770;&middot;x<sub>j</sub>
    * = -y(1-y&#770;)x<sub>j</sub>-(1-y) &middot; (1-y&#770;)/(1-y&#770;) &middot;y&#770;&middot;x<sub>j</sub>
    * = -y(1-y&#770;)x<sub>j</sub>-(1-y)&middot;y&#770;&middot;x<sub>j</sub>
    * = -y(1-y&#770;)x<sub>j</sub> + (1-y)y&#770;x<sub>j</sub>
    * = (-y +y&middot;y&#770;)x<sub>j</sub> + (y&#770; -y&middot;y&#770;)x<sub>j</sub>
    * = -y&middot;x<sub>j</sub> + y&middot;y&#770;&middot;xj<sub></sub> + y&#770;&middot;x<sub>j</sub> -y&middot;y&#770;&middot;x<sub>j</sub>
    * = -y&middot;x<sub>j</sub> + y&#770;&middot;x<sub>j</sub>
    * = **-(y+y&#770;)&middot;x<sub>j</sub>**

### Error at point x Derivative w.r.t bias b 
E = −yln( y&#770;)−(1−y)ln(1− y&#770;)

&part;/&part;b E = -(y-y&#770;)

Derivation:
* &part;/&part;b E = &part;/&part;b[−yln( y&#770;)−(1−y)ln(1− y&#770;)]
    * = =-y&part;/&part;blog(y&#770;) - (1-y)&part;/&part;b log(1-y&#770;)
    * = -y&middot;1/y&#770; &middot; &part;/&part;b y&#770; - (1-y) &middot; 1/(1-y&#770;) &middot; &part;/&part;b (1-y&#770;)
    * = -y &middot; 1/y&#770; &middot; y&#770; &middot;(1-y&#770;)-(1-y)&middot;1/(1-y&#770;)&middot; -1 &middot;y&#770;&middot;(1-y&#770;)
    * = -y&middot;(1-y&#770;) - (1-y)&middot;(1-y&#770;)/(1-y&#770;) &middot; -1 &middot; y&#770;
    * = -y&middot;(1-y&#770;)-(1-y)&middot;-y&#770;
    * = -y&middot;(1-y&#770;)+y&#770;&middot;(1-y)
    * = -y+y&middot;y&#770; + y&#770; - y&middot;y&#770;
    * = -y +y&#770;
    * = **-(y-y&#770;)**

### Gradient of Error at point
For a point with coordinates (x<sub>1</sub>,...,x<sub>n</sub>), label y and prediction y&#770;
* Gradient of error function at point x = (-(y-y&#770;)&middot;x<sub>1</sub>,...,-y(y-y&#770;)&middot;x<sub>n</sub>, -(y-y&#770;))
* &nabla;E = -(y-y&#770;)&middot;(x<sub>1</sub>,...,x<sub>n</sub>, 1)

Gradient is a **scalar times the coordinates of the point**
* Scalar = multiple of **the difference** between the label and the prediction
* Closer the label to the prediction = smaller gradient
* Farther the label from the prediction = larger gradient

### Gradient Descent Step
Subtracting a multiple of the gradient of the error function at every point to update weights.

w'<sub>i</sub> = w<sub>i</sub> - &alpha;[-(y-y&#770;)x<sub>i</sub>]
* = w'<sub>i</sub> = w<sub>i</sub> + &alpha;(y-y&#770;)x<sub>i</sub>

b' = b + &alpha;(y-y&#770;)x<sub>i</sub>

Note: &alpha; is a constant that also that takes into account the 1/m term for averages. Could be written as 1/m &middot; &alpha;