# Sobel Filters

Filters for edge detection and finding patterns in intensity.

Takes an **approximation of the derivative** of the image in the _x_ or _y_ direction.

* Derivative is a measurement of intensity change
  * Gradients in image measure change in intensity
  * For an image given by funciton F(x,y), gradient is the derivative operation F'(x,y)

Sobel<sub>x</sub> and Sobel<sub>y</sub>:

* ![](../../../images/2018-03-20-17-49-56.png)
* x-direction emphasizes vertical edges
* y-direction emphasizes horizontal edges

![](../../../images/2018-03-20-17-50-25.png)

## Magnitude

Detect which edges are strongest. Given by the magnitude (absolute value) of the gradient:

* abs_sobelx = sqrt((sobel<sub>x</sub>)<sup>2</sup>)
* abs_sobely = sqrt((sobel<sub>y</sub>)<sup>2</sup>)
* abs_sobelxy = sqrt((sobel<sub>x</sub>)<sup>2</sup>+(sobel<sub>y</sub>)<sup>2</sup>))

## Direction

Find edges in a particular direction i.e edges that only angle upwards or point left.

Direction of gradient = tan<sup>-1</sup>(sobel<sub>y</sub>/sobel<sub>x</sub>)
