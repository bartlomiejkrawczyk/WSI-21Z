from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np
from cec2017.functions import f1
from typing import Callable


def plot_contour_chart_3d(
        axes: plt.Axes,
        function: Callable[['np.ndarray[float]'], float],
        furthest_point: float) -> None:

    plot_step = furthest_point / 200

    x_arr = y_arr = np.arange(-furthest_point, furthest_point, plot_step)

    X, Y = np.meshgrid(x_arr, y_arr)
    Z = np.empty(X.shape)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = function(np.array([X[i, j], Y[i, j]]))

    axes.contour3D(X, Y, Z, 40)
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.set_zlabel('z')
    axes.set_xlim3d(-furthest_point, furthest_point)
    axes.set_ylim3d(-furthest_point, furthest_point)
    axes.set_title('3D contour')


def add_plot(
        axes: plt.Axes,
        function: Callable[['np.ndarray[float]'], float],
        X: 'np.ndarray[float]', Y: 'np.ndarray[float]') -> None:

    axes.plot(X, Y, [function([x, y])
              for x, y in zip(X, Y)], color='r', marker='.')


def draw_3d_function_with_plot(
        function: Callable[['np.ndarray[float]'], float],
        points: 'np.ndarray[np.ndarray[float]]') -> None:

    axes = plt.axes(projection='3d')
    furthest_point = max([max([abs(n) for n in x]) for x in points])

    plot_contour_chart_3d(axes, function, furthest_point * 1.25)

    points = list(zip(*points))
    add_plot(axes, function, points[0], points[1])

    plt.show()


def main():
    draw_3d_function_with_plot(
        f1, [np.random.uniform(-10, 10, size=2) for _ in range(10)])


if __name__ == '__main__':
    main()
