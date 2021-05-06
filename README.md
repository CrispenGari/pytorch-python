# Pytorch Python

Introduction to machine learning library based on the Torch library, used for applications such as computer vision and natural language processing, primarily developed by Facebook's AI Research lab

## Installation

To install `pytorch` on windows run the following command:

```
pip install torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
```

OR visit the Installation [Docs](https://pytorch.org/get-started/locally/) for your machine:

## TORCH

- The torch package contains data structures for multi-dimensional tensors and defines mathematical operations over these tensors. Additionally, it provides many utilities for efficient serializing of Tensors and arbitrary types, and other useful utilities.

* [Docs](https://pytorch.org/docs/stable/torch.html)

> Examples in the Jupyter Notebook

## Math Operations
### Pointwise Ops
```
a = torch.tensor([2, 8, -9, 0, -17, 67])
b = torch.tensor([1, 2, 3, 4, 5])
c = torch.tensor([9, 8, 7, 6, 5])
d = torch.tensor([1,1, 0, 1, 0, 0, 0, 1])
e = torch.tensor([0,0, 0, 1, 0, 0, 0, 1])
f = torch.rand(12)
```

#### 1. torch.abs()
* Computes the absolute value of each element in input.
```
# abs()
print(torch.abs(a))
```
#### 2. torch.absolute()
* Alias for torch.abs()
```
# absolute()
print(torch.absolute(a))
```
#### 3. torch.acos() || torch.acosh()
* Computes the inverse cosine of each element in input.
```
print(torch.arccos(a))
```
#### 4. torch.add() || torch.div() [torch.divide()] || torch.mul() [torch.multiply()] || torch.sub()[torch.subtract()]
* performs the scalar other to each element of the input input and returns a new resulting tensor.
```
print(torch.add(b, c))
print(c + b)
```
#### 5. torch.max() || torch.min()
* returns the maximum and minimum values in a tensor
```
print(torch.max(a), torch.min(a))
print(a.min(), a.max())
```
#### 6. torch.bitwise_not() || torch.bitwise_and() || torch.bitwise_or() || torch.bitwise_xor()
* Computes the bitwise operations on tensors
```
print(torch.bitwise_or(d, e))
print(torch.bitwise_xor(d, e))
print(torch.bitwise_and(d, e))
print(torch.bitwise_not(d))
```
#### 7. torch.ceil() || touch.floor()
* rounds up or down a tensor and return a result.
```
print(torch.ceil(f))
print(torch.floor(f))
```
#### 8. torch.clamp() || clip()
* Clamp all elements in input into the range [ min, max ].
```
print(torch.clamp(a.float(), 0, 3))
```
#### 9. torch.conj()
* Computes the element-wise conjugate of the given input tensor.
```
print(torch.conj(a.reshape(3, -1)))
```
> There are a lot of these Pointwise Ops in the documentation

### Reduction Ops

#### 1. torch.abs()
* Computes the absolute value of each element in input.
```

```
#### 1. torch.all() || torch.any()
* Tests if all or one element(s) in input evaluate to True.
```
print(torch.all(d))
print(torch.any(d))
```
#### 2. torch.mean() || torch.mode() || torch.median() || torch.std() || torch.var()
* Computes the absolute value of each element in input.
```
print(torch.mean(b.float()))
print(torch.mode(b))
print(torch.median(b))
```
#### 3. torch.unique()
* Returns the unique elements of the input tensor.
```
print(torch.unique(a))
print(a.unique())
```
#### 4. torch.argmax() || torch.argmin()
* Returns the indices of the maximum || minimum value of all elements in the input tensor.
```
print(torch.argmax(a), torch.argmin(a))
```
#### 4. torch.argmax() || torch.argmin()
* Returns the indices of the maximum || minimum value of all elements in the input tensor.
```
print(torch.argmax(a), torch.argmin(a))
```
#### 4. torch.argmax() || torch.argmin()
* Returns the indices of the maximum || minimum value of all elements in the input tensor.
```
print(torch.argmax(a), torch.argmin(a))
```
> There are a lot of these in the documentation

* Comparison Ops
* Spectral Ops
* Other Operations
* BLAS and LAPACK Operations
* Utilities
* [Documentation Reference](https://pytorch.org/docs/stable/torch.html#math-operations)


## TOUCH.NN

#### 1. torch.abs()
* Computes the absolute value of each element in input.
```

```
#### 1. torch.abs()
* Computes the absolute value of each element in input.
```

```
#### 1. torch.abs()
* Computes the absolute value of each element in input.
```

```
#### 1. torch.abs()
* Computes the absolute value of each element in input.
```

```
#### 1. torch.abs()
* Computes the absolute value of each element in input.
```

```
#### 1. torch.abs()
* Computes the absolute value of each element in input.
```

```
#### 1. torch.abs()
* Computes the absolute value of each element in input.
```

```
#### 1. torch.abs()
* Computes the absolute value of each element in input.
```
print(to
```
