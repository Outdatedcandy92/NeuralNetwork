from IPython import display

import matplotlib.pyplot as plt

plt.ion()

def plot(iterations, accuracy, blck):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training Accuracy')
    plt.xlabel('Iterations')
    plt.ylabel('Accuracy')
    plt.plot(iterations,accuracy)
    plt.show(block=blck)
    plt.pause(0.001)

def plot_save():
    plt.savefig('resources/plot.png')
