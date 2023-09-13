# https://www.pinecone.io/learn/batch-layer-normalization/
# See till now what we were doing is giving single set of input to our neural network 
# in genral when we are giving single input to our model the deviation from previous regression line is more
# so to reduce this deviation we are using batch  also called mini batch
# so in this we are giving batch of input to our model

import numpy as np

inputs =  [[1,2,3,2.5],
           [2.0,5.0,-1.0,2.0],
           [-1.5,2.7,3.3,-0.8]]

weights = [[0.2 , 0.8 , -0.5 , 1.0],
           [0.5 , -0.91 , 0.26 , -0.5],
           [-0.26 , -0.27 , 0.17 , 0.87]]

biases = [2,3,0.5]

output = np.dot(inputs,np.array(weights).T) + biases
print(output)