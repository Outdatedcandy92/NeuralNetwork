import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import io

with open('./resources/model_parameters.json', 'r') as json_file:
    loaded_parameters = json.load(json_file)

W1 = np.array(loaded_parameters["W1"])
b1 = np.array(loaded_parameters["b1"])
W2 = np.array(loaded_parameters["W2"])
b2 = np.array(loaded_parameters["b2"])

data = pd.read_csv('./resources/output.csv') 

data = np.array(data)
m, n = data.shape
np.random.shuffle(data) # shuffle before splitting into dev and training sets

data_dev = data[0:1000].T
Y_dev = data_dev[0]
X_dev = data_dev[1:n]
X_dev = X_dev / 255.

data_train = data.T
Y_train = data_train[0]
X_train = data_train[1:n]
X_train = X_train / 255.
_,m_train = X_train.shape

def init_params():
    W1 = np.random.rand(10, 784) - 0.5
    b1 = np.random.rand(10, 1) - 0.5
    W2 = np.random.rand(10, 10) - 0.5
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



def get_predictions(A2):

    return np.argmax(A2, 0)

def get_accuracy(predictions, Y):
    return np.sum(predictions == Y) / Y.size

def make_predictions(X, W1, b1, W2, b2):
    _, _, _, A2 = forward_prop(W1, b1, W2, b2, X)
    predictions = get_predictions(A2)
    A2_normalized = (A2 - np.min(A2)) / (np.max(A2) - np.min(A2))
    A2_normalized = np.round(A2_normalized, 2)  # Round to 2 decimal places

    #print(A2_normalized_str)
    return predictions, A2_normalized



def test_prediction(index, W1, b1, W2, b2):
    current_image = X_train[:, index, None]
    prediction, Neuron_act = make_predictions(X_train[:, index, None], W1, b1, W2, b2)
    label = Y_train[index]
    print("Prediction: ", prediction)
    
    current_image = current_image.reshape((28, 28)) * 255
    plt.gray()
    plt.imshow(current_image, interpolation='nearest')
    plt.title(f"Prediction {prediction}")
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    buf.seek(0)
    return prediction, Neuron_act , buf 

#test_prediction(0, W1, b1, W2, b2)

