#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np

# ToDo tu prosze podac pierwsze cyfry numerow indeksow
p = [3, 7]

L_BOUND = -5
U_BOUND = 5


def q(x):
    return np.sin(x*np.sqrt(p[0]+1))+np.cos(x*np.sqrt(p[1]+1))


x = np.linspace(L_BOUND, U_BOUND, 100)
y = q(x)

np.random.seed(1)


# f logistyczna jako przykĹad sigmoidalej
def sigmoid(x):
    return 1/(1+np.exp(-x))

# pochodna fun. 'sigmoid'


def d_sigmoid(x):
    s = 1/(1+np.exp(-x))
    return s * (1-s)

#f. straty


def nloss(y_out, y):
    return (y_out - y) ** 2

# pochodna f. straty


def d_nloss(y_out, y):
    return 2*(y_out - y)


class DlNet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.y_out = 0

        self.HIDDEN_L_SIZE = 9
        self.LR = 0.003

# ToDo

    def forward(self, x):
        pass
# ToDo

    def predict(self, x):
        # ToDo
        return

    def backward(self, x, y):
        # ToDo

    def train(self, x_set, y_set, iters):
        for i in range(0, iters):
            # ToDo


nn = DlNet(x, y)
nn.train(x, y, 15000)

yh = []  # ToDo tu umiesciÄ wyniki (y) z sieci


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x, y, 'r')
plt.plot(x, yh, 'b')

plt.show()
