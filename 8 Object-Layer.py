import numpy as np
np.random.seed(0)

# Given below are our batch of inputs we are given 3 input instances 
# And no of neurons in input layer are 4
X =  [[1,2,3,2.5],
      [2.0,5.0,-1.0,2.0],
      [-1.5,2.7,3.3,-0.8]]


# This is a class defining a layer of our neural networks
class Layer_Dense:
    def __init__(self , n_inputs , n_neurons):

        # The randn return a matrix of the dimensions that are passed in parameter
        # 0.10 multiplication is done in order to keep the values in range of -1 to 1
        # https://www.geeksforgeeks.org/numpy-random-randn-python/

        self.weights = 0.10 * np.random.randn(n_inputs , n_neurons)
        self.biases = np.zeros((1 , n_neurons))
        
    def forward(self , inputs):
        self.output = np.dot(inputs , self.weights) + self.biases

layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,2)

layer2.forward(layer1.output)
print(layer2.output)