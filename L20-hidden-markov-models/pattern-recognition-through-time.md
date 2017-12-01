# Pattern Recognition Through Time
Extract and recognize patterns in time series data

## Example: Recognize classes of dolphin whistles

### Varying Frequencies 

Frequencies can vary, but the **pattern** stays the same:
* Raise or lower frequency of whistle

![](../images/2017-11-29-08-36-16.png)

Solution: Use **change in frequency**, &Delta;F to define **patterns**:

![](../images/2017-11-29-08-37-07.png)

### Time Warping
Same pattern can be present over different time intervals:
* i.e. saying 'Hello' or 'Helloooooooo'

Need to recognise **features** whether they are drawn out or produced quickly:

![](../images/2017-11-29-08-39-19.png)

#### Euclidean Distance
Make samples same length:
* Pad shorter with 0s

Calculate euclidean distance between all the points:

![](../images/2017-11-29-08-41-04.png)
= Sqrt(170) = approx. **13**

**Insufficient**: very sensitive to distortion in the time axis

#### Dynamic Time Warping
Calculates an **optimal match** between two time series with certain restrictions

[Ratanamahatana and Keogh’s “Everything you know about Dynamic Time Warping is Wrong”](http://wearables.cc.gatech.edu/paper_of_week/DTW_myths.pdf)

Sequences are non-linearly **warped** in the time dimenstion to determine a measure of their **similarity** independent of certain non-linear variations in time dimension.

Allows two time series that are similar but **locally out of phase to align in a non-linear manner**.
* Align the samples to where they 'best' match up

Much better than Euclidean:

![](../images/2017-11-29-08-46-23.png)

##### Sakoe Chiba Bounds
DTW can make signals which are very **different** seem more similar than they are.

Sakoe Chiba bounds place upper and lower bounds on the 'best match' values between the two:

![](../images/2017-11-29-08-48-10.png)

Bounds can be calculated **empirically**, set different bounds and use cross-validation to make sure they are reasonable

#### DTW Algorithm
Given two time series, length *n* and *m*:
* Q=q<sub>1</sub>,q<sub>2</sub>...q<sub>n</sub>
* C=c<sub>1</sub>,c<sub>2</sub>...q<sub>m</sub>

Construct an *n*-by-*m* matrix where (ith, jth) element corresponds to the **squared distance d(q<sub>i</sub>,c<sub>i</sub>)=(q<sub>i</sub>-c<sub>i</sub>)<sup>2</sup>**
* Alignment between points q<sub>i</sub> and c<sub>i</sub>

Retrieve a path through the matrix that **minimizes the total cumulative distance between them**

Optimal path that **minimizes warping cost**:
* DTW(Q,C)=min(sqrt(&sum<sub>k</sub><sup>K</sup>w<sub>k</sub>))
* w<sub>k</sub> = matrix element (i,j)<sub>k</sub> that also belongs to kth element of a warping path W - a contiguous set of matrix elements that represent a mapping between Q and C

Use **dynamic programming** to find warping path by evaluating the recurrence:
* &gamma;(i,j) = d(q<sub>i</sub>,c<sub>i</sub>) + min(&gamma;(i-1,j-1), &gamma;(i-1,j), &gamma;(i,j-1))
    * d(i,j) = distance found in the current cell
    * &gamma;(i,j) = cumulative distance of d(i,j) and the minimum cumulative distances from the three adjacent cells

![](../images/2017-11-29-08-58-14.png)