import numpy as np

inputs = [-1.3 , 2.0 , -0.3 , 1.44 , 100 , 5]
outputs = []

# Very simple implementation if the value is less than 0 make it 0
# as simple as that 
# 
# ReLU Activation Function 
for i in inputs:
    outputs.append(max(0,i))
