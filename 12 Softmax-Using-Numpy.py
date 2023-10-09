import numpy as np
# See till now we know that at last layer we require softmax activation 
# and we also know why we need it
exp_values = []
layer_outputs = [[4.8 , 1.21 , 2.385],
                 [8.9 , -1.81 , 0.2],
                 [1.41 , 1.051 , 0.026]]

exp_values = np.exp(layer_outputs)


