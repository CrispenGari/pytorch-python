## TORCH.AUTOGRAD

``torch.autograd`` is PyTorch’s automatic differentiation engine that powers neural network training.
> [Docs](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html)

**Forward Propagation**: In forward prop, the NN makes its best guess about the correct output. It runs the input data through each of its functions to make this guess.

**Backward Propagation**: In backprop, the NN adjusts its parameters proportionate to the error in its guess. It does this by traversing backwards from the output, collecting the derivatives of the error with respect to the parameters of the functions (gradients), and optimizing the parameters using gradient descent. 
