.2# Here we want to calculate the output of a single node
# which is connected to three neurons in the previous layer

# each neuron has certain value which is provided as an input to next layer neurons
inputs = [1 , 5.1 , 2.1]

# each edge going into the neuron also has its own weight
weights = [3.1 , 2.1 , 8.7]

# every neuron has an associated bias 
# the constant which is added to the product of features and weights. 
# It is used to offset the result. 
# It helps the models to shift the activation function 
# towards the positive or negative side.
bias = 3

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias
print(output)

