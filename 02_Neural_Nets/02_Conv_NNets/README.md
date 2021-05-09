### Convolutional Nueral Networks
A Convolutional Neural Network is type of neural network that is used mainly in image processing applications. Other applications of CNNs are in sequential data such as audio, time series, and NLP. Convolution is one of the main building blocks of a CNN

### Types of CNN operations


1. **1D convolution** — majorly used where the input is sequential such as text or audio.
2. **2D convolution** — majorly used where the input is an image.
3. **3D convolution** — majorly used in 3D medical imaging or detecting events in videos.

### Convolution Operation
> Calculating the convolutional output operation we use the following formular.

<p align="center">
    <img src="https://miro.medium.com/max/330/0*kB2slYSHvL1a0YYX.png" alt="conv"/>
</p>


### Filter/Kernel

In CNN terminology, the 3×3 matrix is called a ‘filter‘ or ‘kernel’ or ‘feature detector’ and the matrix formed by sliding the filter over the image and computing the dot product is called the ‘Convolved Feature’ or ‘Activation Map’ or the ‘Feature Map‘. It is important to note that filters act as feature detectors from the original input image.

### Stride
Stride specifies how much we move the convolution filter at each step.


### Padding
Here we have retained more information from the borders and have also preserved the size of the image.

### Pooling
We apply pooling to reduce dimensionality.

