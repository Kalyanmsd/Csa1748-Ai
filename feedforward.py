import feedforward as np 

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function for backpropagation
def sigmoid_derivative(x):
    return x * (1 - x)

# Feedforward Neural Network Class
class FeedforwardNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases with random values
        self.weights_input_hidden = np.random.uniform(-1, 1, (input_size, hidden_size))
        self.weights_hidden_output = np.random.uniform(-1, 1, (hidden_size, output_size))
        self.bias_hidden = np.random.uniform(-1, 1, (1, hidden_size))
        self.bias_output = np.random.uniform(-1, 1, (1, output_size))

    # Forward pass
    def forward(self, X):
        # Input to hidden layer
        self.hidden_layer_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_layer_output = sigmoid(self.hidden_layer_input)

        # Hidden to output layer
        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output) + self.bias_output
        output = sigmoid(self.output_layer_input)

        return output

    # Backpropagation and weight update
    def backward(self, X, y, output, learning_rate):
        # Calculate error in the output layer
        output_error = y - output
        output_delta = output_error * sigmoid_derivative(output)

        # Calculate error in the hidden layer
        hidden_layer_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_layer_delta = hidden_layer_error * sigmoid_derivative(self.hidden_layer_output)

        # Update weights and biases
        self.weights_hidden_output += np.dot(self.hidden_layer_output.T, output_delta) * learning_rate
        self.weights_input_hidden += np.dot(X.T, hidden_layer_delta) * learning_rate
        self.bias_hidden += np.sum(hidden_layer_delta, axis=0, keepdims=True) * learning_rate
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate

    # Training the network
    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output, learning_rate)

            # Loss (Mean Squared Error)
            loss = np.mean(np.square(y - output))
            if epoch % 1000 == 0:
                print(f'Epoch {epoch}, Loss: {loss}')

# Example Usage: XOR Problem

# Input dataset (XOR logic gates input)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Output dataset (XOR logic gates output)
y = np.array([[0], [1], [1], [0]])

# Initialize Feedforward Neural Network
input_size = 2  # Two input neurons
hidden_size = 2  # Two hidden neurons (can be changed)
output_size = 1  # One output neuron

nn = FeedforwardNeuralNetwork(input_size, hidden_size, output_size)

# Train the network
epochs = 10000
learning_rate = 0.1
nn.train(X, y, epochs, learning_rate)

# Testing the network after training
print("\nPredicted outputs after training:")
for input_data in X:
    print(f"Input: {input_data} -> Predicted Output: {nn.forward(input_data)}")
