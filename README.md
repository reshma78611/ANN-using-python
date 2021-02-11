# ANN (Artificial Neural Networks)

Artificial neural networks are multi-layer networks of neurons that we use to classify things, make predictions, etc.It models the relationship between a set of input signal and output signal.

The artificial neuron have weighted input,threshold values,activation function and an output.

## Perceptron:
It is single layer Neural Network. The single layer neural network  perceptron is applicable for linearly seperable data.It calculated weighted sum of inputs values.The perceptron outputs non zero value only when weighted sum exceeds a certain threshold value.If we consider two inputs as (x,y) on a plane,then perceptron tells us which region on plane to which this points belongs.Such regions are linearly seperable regions.

If data is not linearly seperable we need more than one perceptron.

The information is constantly fed forward from one layer to the next thus this networks are also called **feed forward network**

## Back propogation:
The goal of back propogation in neural networks is to optimize the weights so weights so that the neural network can learn how to correctly map arbitrary inputs and outputs

Options that are empirically determined in Neural network:

1)	Number of Hidden Layers.
2)	Number of neurons in each hidden layer
3)	Activation Function
4)	Error/Loss Function
5)	Gradient descent methods. 

## Convolution Neural Networks:-
Convolution Neural Network (CNN) are powerful artificial neural network technique.It preserve the spatial structure of the problem and were developed for object recognition task such as handwritten digit recognition.There are three types of layers in convolution neural network:-
a)	Convolution layers.
b)	Pooling layers.
c)	Fully Connected layers. 

Using keras tuner we can decide about how many layers to use, how many neurons to use, what activation function to use that is which of them will give the best model.


## Data used 
            Forestfires dataset  : To predict the burned area of forest fires with neural network.
            pima-indians-diabetes : To classify diabetes data
## Programming
            Python
            

**The Codes regarding  Neural Networks  *to predict burnt area of forest fires with forest fires dataset, to classify Pima indians diabetes using pima-indians-diabetes* are present in this Repository in detail.**



