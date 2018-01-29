# Convolutional Layer Dimensionality

## Formula: Number of Paramaters in a Convolutional Layer
number of parameters = `K*F*F*D_in+K`
* Where:
    * K=number of filters
    * F = height and width of layers
    * D_in = depth of previous layer

Explanation:
* Each filter has `F*F*D_in` weights
* Layer is composed of `K` filters
* Total number of weights = `K*F*F*D_in`
* One bias term per filter &rarr; layer has `k` biases
* &rarr; total parameters = `K*F*F*D_in+K`

## Formula: Shape of Convolutional Layer 
Variables:
* K = number of filters in layer
* F = height and width of filters
* S = stride
* H_in = height of previous layer
* W_in = width of previous layer

**Depth** of layer always equals number of filters `K`

If `padding='same'`:
* Height = `ceil(float(H_in)/float(S))`
* Width = `ceil(float(W_in)/float(S))`

If `padding='valid'`:
* Height = `ceil(float(H_in-F+1)/float(S))`
* Width = `ceil(float(W_in-F+1)/float(S))`

## Examples
```Python
from keras.models import Sequential
from keras.layers import Conv2D

model = Sequential()
model.add(Conv2D(filters=16, kernel_size=2, strides=2, padding='valid',
                 activation='relu', input_shape=(200, 200, 1)))
model.summary()
```
* Number of parameters = `16*2*2*1+16 = 80`
* Shape of layer:
    * Height = `ceil(float(200-2+1)/float(2)) = 100`
    * Width = `ceil(float(200-2+1)/float(2)) = 100`
    * Depth = number of filters = 16
Output:
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
conv2d_1 (Conv2D)            (None, 100, 100, 16)      80
=================================================================
Total params: 80.0
Trainable params: 80
Non-trainable params: 0.0
_________________________________________________________________

```

```Python
from keras.models import Sequential
from keras.layers import Conv2D

model = Sequential()
model.add(Conv2D(filters=32, kernel_size=3, strides=2, padding='same',
                 activation='relu', input_shape=(128, 128, 3)))
model.summary()

```
* Number of parameters = `32*3*3*3+32 = 896`
* Shape of layer:
    * Height = `ceil(float(128)/float(2)) = 64`
    * Width = `ceil(float(128)/float(2)) = 64`
    * Depth = number of filters = 32
Output:
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
conv2d_1 (Conv2D)            (None, 64, 64, 32)        896
=================================================================
Total params: 896.0
Trainable params: 896
Non-trainable params: 0.0
_________________________________________________________________
```