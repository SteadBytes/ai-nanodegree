# Perceptrons
* Encoding of equation Wx+b ([boundaries](./linear-boundaries.md)) as a graph
    * Inputs: nodes w/values x<sub>1<sub>-x<sub>n</sub> and corresponding edge weights w<sub>1</sub>-w<sub>n</sub>
    * **Linear function** node calculates Wx+b:
        * Wx+b = &sum;<sup>n</sup><sub>i=1</sub>W<sub>i</sub>x<sub>i</sub> + b
    * **Step function** node calculates result:
        * Return 1 if input is >= 0
        * Return 0 if input < 0

    ![](../../images/2018-01-12-11-26-59.png)
* Bias unit can be an input node w/value of 1 and weight *b* or the bias can be inside the node:
    * ![](../../images/2018-01-12-11-28-26.png)
* Algorithm for learning a binary classifier

## Perceptrons as Logical Operators
Combine perceptrons using different weights and biases to produce logical operators

### AND
![](../../images/2018-01-12-12-25-28.png)
* w<sub>1</sub> = 1
* w<sub>2</sub> = 1
* b = -2

### OR
![](../../images/2018-01-12-12-26-34.png)
![](../../images/2018-01-12-12-26-51.png)
* Increase both weights OR decrease magnitude of bias

### NOT
* Only cares about 1 input
    * Inverts it: 1->0, 0->1

![](../../images/2018-01-12-12-38-39.png)
* w<sub>1</sub> = 0
    * Ignore first input
* w<sub>2</sub> = -1
    * Invert second input
* b = 0.5

### NAND
* AND followed by NOT

### XOR
![](../../images/2018-01-12-12-40-38.png)
![](../../images/2018-01-12-12-39-30.png)


