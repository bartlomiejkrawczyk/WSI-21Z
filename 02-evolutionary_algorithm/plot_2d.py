from matplotlib import pyplot as plt
import numpy as np
from typing import Callable, List


def plot_contour_chart_2d(
        function: Callable[[List[float]], float],
        furthest_point: float) -> None:

    furthest_point = max([abs(x) for x in plt.xlim()] +
                         [abs(y) for y in plt.ylim()] +
                         [furthest_point])

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
            Z[i, j] = function([X[i, j], Y[i, j]])

    plt.contour(X, Y, Z, 40)
    plt.colorbar()


def main():
    pass


if __name__ == '__main__':
    main()
