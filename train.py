import numpy as np
from plot import plot,plot_save
import pandas as pd
import json

data = pd.read_csv('./resources/mnist_train.csv')

data = np.array(data)
m, n = data.shape
np.random.shuffle(data) # shuffle before splitting into dev and training sets

data_train = data[0:m].T
Y_train = data_train[0]
X_train = data_train[1:n]
X_train = X_train / 255.
_,m_train = X_train.shape

# Hyperparameters

LEARNING_RATE = 0.10
ITERATIONS = 500





def init_params():
    W1 = np.random.rand(100, 784) - 0.5
    b1 = np.random.rand(100, 1) - 0.5
    W2 = np.random.rand(10, 100) - 0.5
    b2 = np.random.rand(10, 1) - 0.5
    return W1, b1, W2, b2

def ReLU(Z):
    return np.maximum(Z, 0)

def softmax(Z):
    A = np.exp(Z) / sum(np.exp(Z))
    return A
    
def forward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2

def ReLU_deriv(Z):
    return Z > 0

def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y

def backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y):
    one_hot_Y = one_hot(Y)
    dZ2 = A2 - one_hot_Y
    dW2 = 1 / m * dZ2.dot(A1.T)
    db2 = 1 / m * np.sum(dZ2)
    dZ1 = W2.T.dot(dZ2) * ReLU_deriv(Z1)
    dW1 = 1 / m * dZ1.dot(X.T)
    db1 = 1 / m * np.sum(dZ1)
    return dW1, db1, dW2, db2

def update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha):
    W1 = W1 - alpha * dW1
    b1 = b1 - alpha * db1    
    W2 = W2 - alpha * dW2  
    b2 = b2 - alpha * db2   
    return W1, b1, W2, b2




def get_predictions(A2):

    return np.argmax(A2, 0)

def get_accuracy(predictions, Y):

    return np.sum(predictions == Y) / Y.size

def get_acc(predictions, Y):
    count = 0
    for pred, actual in zip(predictions, Y):
        if pred == actual:
            count += 1
    accuracy = count / len(Y)
    return accuracy

import matplotlib.pyplot as plt  # Ensure matplotlib is imported

def gradient_descent(X, Y, alpha, iterations):
    W1, b1, W2, b2 = init_params()
    iterations_list = []  # List to store iteration numbers
    accuracies_list = []  # List to store accuracies
    for i in range(iterations):
        Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
        dW1, db1, dW2, db2 = backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y)
        W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)
        if i % 10 == 0:
            print("Iteration: ", i)
            predictions = get_predictions(A2)
            accuracy = get_accuracy(predictions, Y)
            print(f"Accuracy: {accuracy * 100:.2f}%")
            iterations_list.append(i)
            accuracies_list.append(round(accuracy * 100, 2))

    plot(iterations_list, accuracies_list, True)  # Plot all points at once
    plot_save()

    return W1, b1, W2, b2


W1, b1, W2, b2 = gradient_descent(X_train, Y_train, LEARNING_RATE, ITERATIONS)

model_parameters = {
    "W1": W1.tolist(),
    "b1": b1.tolist(),
    "W2": W2.tolist(),
    "b2": b2.tolist()
}

with open('./resources/model_parameters.json', 'w') as json_file:
    json.dump(model_parameters, json_file)
    print("Model parameters saved to model_parameters.json")

