# Softmax activation function is generally used at the output layer
# Why do we need to use another activation function in output layer 

# See eventually what we need to do is see how correct is our neural network
# For example we are given two outputs  
# now which of these outputs should be deemed more correct
# layer_outputs1 = [4.8 , 1.21 , 2.385]

# layer_outputs2 = [4.8 , 4.79 , 4.25]
# So we can say the one which differentiaties between 
# the wrong and right more effectively should be more correct outputs i.e. output1
# These outputs are unbounded so each output sample can vary from each other considerably

# Problems with other Activation Function at output layer
# 1 handling of negative value
# 2 unbounded outputs
# 3 samples can vary consideraby

import math
E = math.e

exp_values = []
layer_outputs = [4.8 , 1.21 , 2.385]

# One problem of handling negative value can br solved by exponentiation
# Exponentiation
for output in layer_outputs:
    exp_values.append(E**output)

print(exp_values)

# The other issue can be solved by normalization
# Normalization

norm_base = sum(exp_values)
norm_values = []

for value in exp_values:
    norm_values.append(value / norm_base)

print(norm_values)
print(sum(norm_values))    

