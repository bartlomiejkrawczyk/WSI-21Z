import numpy as np
from cec2017.functions import f1, f2, f3
from plot_3d import draw_3d_function_with_plot
import operator
from typing import Callable


def partial_derivative(
        function: Callable[['np.ndarray[float]'], float],
        point: 'np.ndarray[float]',
        i: int) -> float:

    delta = 1e-10
    new_point = point.copy()
    new_point[i] = point[i] + delta
    return (function(new_point) - function(point)) / delta


def gradient(
        function: Callable[['np.ndarray[float]'], float],
        point: 'np.ndarray[float]') -> 'np.ndarray[float]':

    return np.array([partial_derivative(function, point, i) for i in range(len(point))])


def stop(
        function: Callable[['np.ndarray[float]'], float],
        points: 'np.ndarray[np.ndarray[float]]',
        step_factor: float) -> bool:

    if len(points) > 1000:
        print("Exceeded 1000 points")
        print(points[-1])
        return True

    point = points[-1]
    delta = 1e-3
    value = function(point)

    comparison_function = operator.ge if step_factor > 0 else operator.le

    if (
        comparison_function(value, function(np.add(point, [0, delta]))) and
        comparison_function(value, function(np.add(point, [0, -delta]))) and
        comparison_function(value, function(np.add(point, [delta, 0]))) and
        comparison_function(value, function(np.add(point, [-delta, 0])))
    ):
        print("Found with:", len(points), 'points')
        print(points[-1])
        return True

    return False


def steepest_ascent(
        function: Callable[['np.ndarray[float]'], float],
        point: 'np.ndarray[float]',
        step_factor: float) -> 'np.ndarray[float]':

    grad = gradient(function, point) * step_factor
    return np.add(point, grad)


def steepest_ascent_steps(
        function: Callable[['np.ndarray[float]'], float],
        starting_point: 'np.ndarray[float]',
        step_factor: float) -> 'np.ndarray[np.ndarray[float]]':

    points = [starting_point]

    while not stop(function, points, step_factor):
        points.append(steepest_ascent(function, points[-1], step_factor))

    return points


def steepest_ascent_steps_advanced(
        function: Callable[['np.ndarray[float]'], float],
        starting_point: 'np.ndarray[float]',
        step_factor: float) -> 'np.ndarray[np.ndarray[float]]':

    multiplier = 2
    points = [starting_point]
    best = function(starting_point)
    comparison_function = operator.le if step_factor > 0 else operator.ge

    while not stop(function, points, step_factor):
        point = steepest_ascent(function, points[-1], step_factor)
        value = function(point)
        if comparison_function(best, value):
            best = value
            points.append(point)
            step_factor = step_factor * multiplier
        else:
            step_factor = step_factor / multiplier

    return points


def draw_3d_function(
        function: Callable[['np.ndarray[float]'], float],
        step_factor: float) -> None:

    starting_point = np.random.uniform(-10, 10, size=2)

    points = steepest_ascent_steps_advanced(
        function, starting_point, step_factor)

    draw_3d_function_with_plot(function, points)


def main():
    def func(x):
        return x[0] ** 2 + 4 * x[1] ** 2

    functions = [
        (f1, -0.00000001),
        (f1, -0.1),
        (f2, -0.7),
        (f3, -0.00005),
        (func, -0.1)
    ]
    for function, step_factor in functions:
        draw_3d_function(function, step_factor)


if __name__ == '__main__':
    main()
