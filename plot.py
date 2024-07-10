from IPython import display

import matplotlib.pyplot as plt

plt.ion()

def plot(iterations, accuracy, blck):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Data')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(iterations,accuracy)
    plt.show(block=blck)
    plt.pause(0.001)

def plot_final(iterations, accuracy):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Data')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(iterations,accuracy)
    plt.show(block=True)

def save():
    plt.savefig('archive/plot.png')
