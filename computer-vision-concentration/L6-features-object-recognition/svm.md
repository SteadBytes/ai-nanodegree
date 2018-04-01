# Support Vector Machine (SVM)

Supervised learning model for classification and regression analysis.

Given a set of training examples, each belonging to a category, the SVM training algorithm will build a model that assigns new examples to a category.

Represents examples as **points in space**

* Mapped such that examples of separate categories are divied by a clear gap

SVM's compute an **optimal hyperplane** which separates training data

* Optimal hyperplane will give the **maxmimum margin**
  * **largest minimum distance** to the training examples
  * Too close to the points -> noise sensitive, not generalize corectly.

![](../../images/2018-03-30-16-18-54.png)

## Computing the Optimal Hyperplane

A hyperplane is defined as:

![](../../images/2018-03-30-16-27-39.png)

* &beta; = weight vector
* &beta;<sub>0</sub> = bias
* _x_ = trainsing examples

Optimal hyperplane represented as the **canonical hyperplane**:

![](../../images/2018-03-30-16-27-49.png)

* _x_ = training examples _closest_ to the hyperplane
  * Called **support vectors**

Distance between a point _x_ and a hyperplane (&beta;,&beta;<sub>0</sub>):

![](../../images/2018-03-30-16-30-29.png)

For the canonical hyperplane:

![](../../images/2018-03-30-16-30-52.png)

Maximum margin _M_, twice distance to closest examples:

![](../../images/2018-03-30-16-32-16.png)

Maximizing _M_:

![](../../images/2018-03-30-16-33-05.png)

* x<sub>i</sub> = each of the training examples
* y<sub>i</sub> = each of the **labels** of the training examples
* **Lagrangian Optimization**
  * Solved using Lagran multipliers to obtain weight vector and bias of optimal hyperplane

## Resources:

* http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_ml/py_svm/py_svm_opencv/py_svm_opencv.html
* https://en.wikipedia.org/wiki/Support_vector_machine
