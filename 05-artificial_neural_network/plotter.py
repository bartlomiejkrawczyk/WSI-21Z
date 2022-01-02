from numpy import typing as npt
from matplotlib import pyplot as plt
import numpy as np


def plot_functions(x: npt.NDArray[np.float64], y: npt.NDArray[np.float64], approximated_y: npt.NDArray[np.float64]):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x, y, 'r')
    plt.plot(x, approximated_y, 'b')

    plt.show()
