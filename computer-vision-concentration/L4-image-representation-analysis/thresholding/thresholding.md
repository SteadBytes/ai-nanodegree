# Thresholding

Image Processing technique for **image segmentation** to partition an image into multiple segments that are easier to analyze.

Basic Definition for a Grayscale image:

* Given intensity for a pixel at location (i, j) _I<sub>i,j</sub>_ and a fixed constant intensity value _T_
* For each pixel (i,j) in the image:
  * If _I<sub>i,j</sub>_ < _T_:
    * Replace with a black pixel
  * Else if _I<sub>i,j</sub>_ > _T_:
    * Replace with white pixel

![](../../../images/2018-03-17-11-26-42.png)

* [source](<https://en.wikipedia.org/wiki/Thresholding_(image_processing)>)

## Color Thresholds

Designate a separate threshold for each of the RGB components of the image, then **combine them with an AND operation**.

## Color Spaces

![](../../../images/2018-03-17-18-42-24.png)

RGB color selection depends on **even lighting and consistent color**:

* Easy to select the blue background:
  * ![](../../../images/2018-03-17-18-40-57.png)
* Simple blue colour threshold won't work:
  * ![](../../../images/2018-03-17-18-41-35.png)

HSV is more reliable for detecting coloured objects:

* ![](../../../images/2018-03-17-18-43-37.png)

See jupyter notebooks for examples
