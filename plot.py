import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(iterations, accuracy):
    Yaxis = round(int(accuracy) * 100, 2)
    Xaxis = int(iterations)
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Data')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(Xaxis, Yaxis)
    plt.ylim(ymin=0)
    plt.show(block=False)
    plt.pause(.1)

def save():
    plt.savefig('data/plot.png')