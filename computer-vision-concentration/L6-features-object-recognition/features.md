# Features in Computer Vision

**Feature** = a measurable piece of data in an image

* Distinct colour
* Line
* Edge
* Image segment

## Good Features

Should be easily compared and traked among images of the same object or scene

* Consistent across scales, lighting conditions and angles
* Can be identified in noisy images

Feature extraction **reduces dimensionality** of the image data:

* Isolate specific colour/spatial information
* Transform large sets of image data to smaller sets of features

## Feature Types

* Edges
  * Areas with a high intensity gradient
* Corners
  * Intersection of two edges
* Blobs
  * Region-based features -> areas of extreme intensity or unique texture

**Corners** match _exactly_ and are good features

* Represent a point where two edges change, moving the two edges will make the corner not match
  * Can determine exactly where the corner should be

### Example

![](../../images/2018-03-27-10-59-38.png)

![](../../images/2018-03-27-10-59-53.png)

Which area do the patches match with?

#### **A**

![](../../images/2018-03-27-11-00-23.png)

Blank white blob, could be anywhere within multiple sections of the image

* Doesn't have very good features

#### **B**

![](../../images/2018-03-27-11-01-16.png)

![](../../images/2018-03-27-11-01-29.png)

B contains an **edge**. It's orientation means it must be along the boundary between the bottom white section and the red section.

**However**, it could be _anywhere_ along that edge, so it's exact position cannot be determined

* Can only approximate

#### **C**

![](../../images/2018-03-27-11-02-53.png)

C contains a **corner**, can be matched **exactly** to the position in the bottom right

## Corner Detection

Corners have **large variation in intensity in all directions**

* Large gradient in all directions

**Sobel Operators/Filters** approximate the gradients of the image in _x_ and _y_ direction seperately:

![](../../images/2018-03-27-11-29-58.png)

![](../../images/2018-03-27-11-30-10.png)

Magnitude and direction from Sobel operators using **Polar Coordinates**:
(used in Hough Transform)

![](../../images/2018-03-27-11-32-17.png)

![](../../images/2018-03-27-11-33-33.png)

![](../../images/2018-03-27-11-33-24.png)

![](../../images/2018-03-27-11-34-06.png)

* G<sub>x</sub> = Sobel<sub>x</sub> = gradient in _x_ direction
* G<sub>y</sub> = Sobel<sub>y</sub> = gradient in _y_ direction

After applying above:

![](../../images/2018-03-27-11-35-14.png)

Apply windowing to the image:

* Shift a window around an area in the image
* Check for a **large variation** in the directino and magnitude of the gradient
