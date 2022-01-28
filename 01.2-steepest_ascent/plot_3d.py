from matplotlib import pyplot as plt
import numpy as np
from cec2017.functions import f1
from typing import Callable, List, TYPE_CHECKING, Any

if TYPE_CHECKING:
    NDArrayFloat = np.ndarray[Any, np.dtype[np.float64]]
else:
    NDArrayFloat = Any


def plot_contour_chart_3d(
        axes: plt.Axes,
        function: Callable[[NDArrayFloat], float],
        furthest_point: float,
        function_name: str) -> None:

    plot_step = furthest_point / 200

    x_arr = y_arr = np.arange(  # type: ignore
        -furthest_point,
        furthest_point,
        plot_step
    )

    X, Y = np.meshgrid(x_arr, y_arr)  # type: ignore
    Z = np.empty(X.shape)  # type: ignore

    for i in range(X.shape[0]):  # type: ignore
        for j in range(X.shape[1]):  # type: ignore
            Z[i, j] = function(np.array([X[i, j], Y[i, j]]))  # type: ignore

    axes.contour3D(X, Y, Z, 40)
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.set_zlabel('z')
    axes.set_xlim3d(-furthest_point, furthest_point)
    axes.set_ylim3d(-furthest_point, furthest_point)
    axes.set_title(function_name)


def add_plot(
        axes: plt.Axes,
        function: Callable[[NDArrayFloat], float],
        X: NDArrayFloat, Y: NDArrayFloat) -> None:

    axes.plot(
        X, Y,
        [
            function(np.array([x, y]))   # type: ignore
            for x, y in zip(X, Y)
        ],
        color='r',
        marker='.'
    )


def draw_3d_function_with_plot(
        function: Callable[[NDArrayFloat], float],
        points: List[NDArrayFloat],
        function_name: str = 'Contour 3D') -> None:

    axes = plt.axes(projection='3d')
    furthest_point = max([max([abs(n) for n in x]) for x in points])

    plot_contour_chart_3d(axes, function, furthest_point * 1.25, function_name)

    points = np.array(list(zip(*points)))   # type: ignore
    add_plot(axes, function, points[0], points[1])

    plt.show()


def main():
    draw_3d_function_with_plot(
        f1,   # type: ignore
        [np.random.uniform(-10, 10, size=2) for _ in range(10)]
    )


if __name__ == '__main__':
    main()
