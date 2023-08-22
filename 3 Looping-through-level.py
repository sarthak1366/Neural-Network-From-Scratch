inputs = [1,2,3,2.5]

# So in this section also we are dealing with a level 
# having 4 neurons in previous layer and 3 neurons in next layer/ouput layer for now

# Now as we have 4 neurons in previous layer therefore 
# the next layer neuron will have 4 weights comming in 
# there are 3 neurons in output layer therefore each of them will have 4 weights comming in
# 3 list of weights

weights = [[0.2 , 0.8 , -0.5 , 1.0],
           [0.5 , -0.91 , 0.26 , -0.5],
           [-0.26 , -0.27 , 0.17 , 0.87]]

# each output neuron will have its own bias
biases = [2,3,0.5]

# it will contain output for the three neurons with which we are dealing right now
layer_ouput = []

# the zip function will club respective elements from each list
# i.e weights[0](which itself is a vector) gets clubbed with biases[0]

for neuron_weight , neuron_bias in zip(weights , biases) : 
    # So in zip the values will be like so
    # [ [ [0.2 , 0.8 , -0.5 , 1.0] , 2 ] , [...] , ...]
    neuron_output = 0
    for neuron_input , weight in zip(inputs , neuron_weight) :
        # in here what we are doing is we have weights for first neuron
        # we want to multiply each with corresponding inputs
        # finally at the end we will add the bias
        neuron_output += neuron_input*weight
    neuron_output += neuron_bias
    layer_ouput.append(neuron_output)

print(layer_ouput)