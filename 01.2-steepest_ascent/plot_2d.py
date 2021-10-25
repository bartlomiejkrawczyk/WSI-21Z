from matplotlib import pyplot as plt
import numpy as np
from typing import Callable
from math import sqrt


def plot_contour_chart_2d(
        function: Callable[['np.ndarray[float]'], float],
        furthest_point: float) -> None:

    plot_step = furthest_point / 200

    x_arr = y_arr = np.arange(-furthest_point, furthest_point, plot_step)
    X, Y = np.meshgrid(x_arr, y_arr)
    Z = np.empty(X.shape)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = function(np.array([X[i, j], Y[i, j]]))

    contour = plt.contour(X, Y, Z, 20)
    plt.clabel(contour, inline=1, fontsize=10)


def add_arrow(point: 'np.ndarray[float]', next: 'np.ndarray[float]'):
    dx = next[0] - point[0]
    dy = next[1] - point[1]
    length = sqrt(dx ** 2 + dy ** 2)
    head_width = length / 30
    head_length = length / 15
    plt.arrow(point[0], point[1],
              dx * (length - head_length) / length,
              dy * (length - head_length) / length,
              head_width=head_width,
              head_length=head_length, fc='k', ec='k')


def draw_2d_function_with_arrows(
        function: Callable[['np.ndarray[float]'], float],
        points: 'np.ndarray[np.ndarray[float]]') -> None:

    furthest_point = max([max([abs(n) for n in x]) for x in points])
    plot_contour_chart_2d(function, furthest_point * 1.25)

    for i in range(len(points) - 1):
        add_arrow(points[i], points[i + 1])

    plt.show()


def main():
    draw_2d_function_with_arrows(lambda x: (
        x[0]**2 + x[1] ** 2), [np.random.uniform(-10, 10, size=2) for _ in range(10)])


if __name__ == '__main__':
    main()
