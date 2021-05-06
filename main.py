import os
import torch
import numpy as np
from matplotlib import pyplot as plt

device = "cude" if torch.cuda.is_available() else "cpu"
# Mathematical operations
a = torch.tensor([2, 8, -9, 0, -17, 67], device=device)
b = torch.tensor([1, 2, 3, 4, 5])
c = torch.tensor([9, 8, 7, 6, 5])
d = torch.tensor([1,1, 0, 1, 0, 0, 0, 1])
e = torch.tensor([0,0, 0, 1, 0, 0, 0, 1])
f = torch.rand(12)
# abs()
print(torch.abs(a))

# absolute()
print(torch.absolute(a))

# torch.acos() || torch.acosh()
print(torch.arccos(a))

# torch.add()
print(torch.add(b, c))
print(c + b)

# max() || min()
print(torch.max(a), torch.min(a))
print(a.min(), a.max())
# torch.bitwise_not() || torch.bitwise_and() || torch.bitwise_or() || torch.bitwise_xor()
print(torch.bitwise_or(d, e))
print(torch.bitwise_xor(d, e))
print(torch.bitwise_and(d, e))
print(torch.bitwise_not(d))

# floor() || ceil()
print(torch.ceil(f))
print(torch.floor(f))

# clamp()

print(torch.clamp(a.float(), 0, 3))

# conj()
print(torch.conj(a.reshape(3, -1)))

## all() || any()
print(torch.all(d))
print(torch.any(d))

## torch.mean() || torch.mode() || torch.median()
print(torch.mean(b.float()))
print(torch.mode(b))
print(torch.median(b))

## torch.argmax() || argmin()

print(torch.argmax(a), torch.argmin(a))