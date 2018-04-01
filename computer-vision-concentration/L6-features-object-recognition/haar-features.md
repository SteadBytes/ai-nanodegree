# Haar Features

Gradient measurements used to **categorize image subsections**:

* Considers adjacent rectangular regions at a specific location in a detection window
* Sums up pixel intensities in each region
* Calculates difference between sums

Detect:

* Edges
* Lines
* Rectangle Patterns

![](../../images/2018-04-01-15-05-25.png)

## Human Face Example

Region of the eyes is darker than the region of the cheeks

* -> Haar feature with two adjacent rectangles lying above the eye and cheek region

![](../../images/2018-04-01-15-07-42.png)

## Computation

**Advantage** of Haar features = can be computed quickly using **integral images/summed-area tables**

### Summed-area Table

Quickly and efficiently sum the values of a **rectangular subse** of a matrix.

Value at an point (x,y) in the summed-area table is the sum of all the pixels **above and to the left** of (x,y), inclusive:

* ![](../../images/2018-04-01-15-13-40.png)
* i(x,y) is the value of the pixel at (x,y)

Summed-area table can be computed in a **single pass** over the image.

Value in the summed-area table at (x,y):

* ![](../../images/2018-04-01-15-14-57.png)

**Once computed**, the sum of intensities over **any rectangulare area** requires **exactly four array references**:

* ![](../../images/2018-04-01-15-16-41.png)
  * A=(x<sub>0</sub>, y<sub>0</sub>)
  * B=(x<sub>1</sub>, y<sub>0</sub>)
  * C=(x<sub>0</sub>, y<sub>1</sub>)
  * D=(x<sub>1</sub>, y<sub>1</sub>)
* Sum of i(x,y) over rectangle A,B,C,D:
  * ![](../../images/2018-04-01-15-18-13.png)
