from matplotlib import pyplot as plt
import numpy as np
from typing import Callable
from steepest_ascent import steepest_ascent_steps_advanced


def plot_2d(
        function: Callable[['np.ndarray[float]'], float],
        furthest_point: float):

    plot_step = furthest_point / 200

    x_arr = np.arange(-furthest_point, furthest_point, plot_step)

    plt.plot(x_arr, [function([x]) for x in x_arr], color='b')


def draw_2d_function_with_plot(func, points):
    plot_2d(func, max([abs(x[0]) for x in points]))
    plt.plot(points, [func(x) for x in points], color='r', marker='.')
    plt.show()


def main():
    def function(x): return x[0] ** 4 - 20 * x[0] ** 2
    draw_2d_function_with_plot(
        function, steepest_ascent_steps_advanced(function, np.random.uniform(-10, 10, size=1), -1))


if __name__ == '__main__':
    main()
