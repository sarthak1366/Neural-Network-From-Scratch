import numpy as np

inputs =  [1,2,3,2.5]

weights = [[0.2 , 0.8 , -0.5 , 1.0],
           [0.5 , -0.91 , 0.26 , -0.5],
           [-0.26 , -0.27 , 0.17 , 0.87]]

biases = [2,3,0.5]

# Let's say you have a 2D array A with shape (m, n) and a 1D array B with shape (n,). The dot product of A and B would result in a 1D array C with shape (m,).

# Here's the general idea of how the dot product works:

# Each row of the 2D array A is treated as a vector.
# The dot product of each row vector of A with the 1D array B is calculated.
# The resulting dot products are placed in the corresponding positions of the resulting 1D array C.

output = np.dot(weights,inputs) + biases
# np.dot(..) returns an array of 3 dim each correspoinding element is than added to each element of biases

print(output)