
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

--- 

## How does it works?

#### 1. We have 28x28 pixel images

![rec](./temp/px.png)

#### 2. Images are converted into a .csv
 For Simplicty we are just looking at an example with 1 number (with random values).

| Label   | 1x1 | 1x2 | 1x3 | ... | 28x28 |
| ------- | --- | --- | --- | --- | --- |
| 9       | 0   | 0   | 153   | ... | 343   |

 
- Here each pixel is given a value between `0` and `255` based on its brightness.
- `0` being black, `255` being complelty white

#### 3. We convert the csv into a matrix

```math
X = \begin{bmatrix}-- X^{[1]}-- \\. \\ .\\.\\--X^{[m]}--\end{bmatrix}^{T}  = 
 \begin{bmatrix} | \  .\ . \ . \ | \\X^{[1]} .. X^{[m]} \\|\  .\ . \ .\  | \\\end{bmatrix}
 ``` 

- Here in the first matrix, each row has 784 values, accounting for the value of each pixel
- We then transpose it and now each column has 784 values
- `m` = the number of examples our training data has

#### -> What we are aiming for

![img](./temp/neural.png)


#### 4. Forward Propogation
- $A^{[0]}$is our input layer 

$ \large A^{[0]}= X$ 

---
- $Z^{[1]}$ is our hidden layer , $w^{[1]}$ is weight, $b^{[1]}$ is bias
 
$ \large Z^{[1]}= w^{[1]}A^{[0]} + b^{[1]}$


#### 5. Activation Function
- We use Rectified Linear Unit here
&nbsp; 
$A^{[1]}= ReLU(Z^{[1]})$   
&nbsp; 
$ReLU(x) = \max(0,x)$
&nbsp; 
#### 6. Layer [1] to [2]
&nbsp; 
```math  
   \large Z^{[2]}= w^{[2]}A^{[1]} + b^{[2]}
```   
&nbsp; 
#### 7. Activation Function for layer 2
&nbsp; 
$A^{[2]}=softmax(Z^{[2]})$ `Output Layer`
&nbsp; 
```math
\text{Output Layer} \begin{bmatrix}1.3 \\. \\\ . \\. \\7.2 \\\end{bmatrix}   \huge  \to \small \text{Softmax Function} \huge \frac{e^{z_{i}}}{\sum_{j=1}^{K}e^{z_{j}}} \to \normalsize  \begin{bmatrix}0.02 \\. \\. \\. \\0.98 \\ \end{bmatrix}\text{Probabilites}
```
&nbsp; 
- Probability values are gonna be between `0` and `1`

#### 8. Back Propogation `Fix Weights and Biases`
&nbsp; 
```math 
\Large \displaystyle 2^{nd} Layer\Large \begin{cases}
dZ^{[2]} = A^{[2]}- Y  \\
dW^{[2]} =\frac{1}{m} dZ^{[2]}A^{[1]^{T}}\\
db^{[2]}=\frac{1}{m}\sum_{}^{}dz^{[2]} \\
\end{cases}
```
&nbsp;
&nbsp;
&nbsp;

```math 
\Large \displaystyle 1^{st} Layer\Large \begin{cases} dZ^{[1]}=W^{[1]^{T}}dZ^{[2]} \times g'(Z^{[1]})\\ dW^{[1]}=\frac{1}{m}dZ^{[1]}X^{T}\\ db^{[1]}=\frac{1}{m}\sum_{}^{}dZ^{[1]}
\end{cases}
```
&nbsp;

#### 9. Updating Weights and Biases

```math
\Large \alpha \normalsize = Learning \ Rate \ \ \ (Hyperparameter)
```
 

$$W^{[1]}= W^{[1]}- \Large \alpha \ \normalsize  dW^{[1]}\\
b^{[1]}= b^{[1]}- \Large \alpha \ \normalsize  db^{[1]}\\
W^{[2]}= W^{[2]}- \Large \alpha \ \normalsize  dW^{[2]}\\
b^{[2]}= b^{[2]}- \Large \alpha \ \normalsize  db^{[2]}\\$$


#### 10. Repeat the process with new weights and biases

 <img src="/temp/flow.png" style="display: block;  margin-left: auto;
  margin-right: auto;">

--- 
