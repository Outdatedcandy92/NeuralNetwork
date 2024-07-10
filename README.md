
# Neural Network From Scratch In Python

This is a neural network made from scratch in python using numpy.

## Installation

Clone the repository

```bash
  > git clone https://github.com/Outdatedcandy92/NeuralNetwork.git
  > cd NeuralNetwork
```
Install requirements
```bash
  > pip install -r requirements.txt
```

    
## Usage

### Step 1: Training

1. Change `LEARNING_RATE` & `ITERATIONS` to your liking or leave it as is.   
`(Around 91% Accuracy on 1000 Iterations at 0.20 LR)`

```python
#Adjust these variables to your liking
LEARNING_RATE = 0.20 
ITERATIONS = 1000
```
2. Run train.py 
   
```bash
> python train.py
```

#### Output:
```python
Iteration:  480
Accuracy: 89.46%
Figure(640x480)
Iteration:  490
Accuracy: 90.17%
Figure(800x600)
```

### Step 2: Testing the model

1. Run draw.py

```bash
> python draw.py
```
2. Inside the pygame window draw a number and then press `S` to get the prediction.   

 
![rec](https://github.com/Outdatedcandy92/NeuralNetwork/assets/138517406/20588d9f-d6b6-4eea-a4d0-35a8bc2a007b)

