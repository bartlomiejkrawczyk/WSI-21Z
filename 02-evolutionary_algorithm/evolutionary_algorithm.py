from typing import Callable, List, Tuple, Any
from cec2017.functions import f4
from random import choices, gauss, random
from plot_2d import plot_contour_chart_2d
from matplotlib import pyplot as plt
from colour import Color  # type: ignore
import heapq
from functools import total_ordering


"""
Data:
    q(x) - function,
    P0 - starting_population,
    µ - population_size,
    σ - mutation_factor,
    pc - cross_probability,
    tmax - max_iterations
Result:
    xˆ∗ - best_subject,
    oˆ∗ - best_rating

"""


@total_ordering
class Point:
    def __init__(self, point: List[float]) -> None:
        self.point = point

    def evaluate(self, function: Callable[[List[float]], float]):
        self.rating = function(self.point)

    def __lt__(self, other: 'Point'):
        return self.rating < other.rating

    def __eq__(self, other: Any):
        return self.rating == other.rating


def reproduction(population: List[Point],
                 population_size: int) -> List[Point]:
    """
    Tournament Selection

    From two points chosen at random the better one is chosen.
    """

    return [
        min(
            choices(population, k=2)
        )
        for _ in range(population_size)]


def genetic_operations(population: List[Point],
                       mutation_factor: float) -> List[Point]:
    """
    Mutation

    For every point choose a random distance in every direction to move.
    Choose closer distance with greater probability.
    """

    return [
        Point([x + gauss(0, 1) * mutation_factor for x in subject.point])
        for subject in population
    ]


def succesion(population: List[Point],
              mutated: List[Point],
              elite_count: int,
              population_size: int) -> List[Point]:
    """
    Elitary Succesion

    From previous population choose the best elite_count subjects.
    Append to them mutated subjects and remove excess (worst)
    individuals to match the population_size number.
    """

    best_population = heapq.nsmallest(elite_count, population)

    return heapq.nsmallest(population_size, best_population + mutated)


def evolve(function: Callable[[List[float]], float],
           starting_population: List[List[float]],
           mutation_factor: float,
           population_size: int,
           elite_count: int,
           max_iterations: int) -> Tuple[List[float], float]:
    """Classical evolutionary algorithm"""

    population = [Point(point) for point in starting_population]
    for p in population:
        p.evaluate(function)
    best = min(population)

    for t in range(max_iterations):
        reproduced = reproduction(population, population_size)

        mutated = genetic_operations(reproduced, mutation_factor)

        for p in mutated:
            p.evaluate(function)

        best_mutated = min(mutated)

        best = min(best, best_mutated)

        if __name__ == '__main__':
            plt.scatter(  # type: ignore
                *zip(*[p.point for p in population]),
                c=COLORS[t].get_hex(),
                marker='.'  # type: ignore
            )

        population = succesion(population, mutated,
                               elite_count, population_size)

    return best.point, best.rating


MAX_FUNCTION_EVALUATIONS = 10_000

MAX_BOUND = 100
FUNCTION: Callable[[List[float]], float] = f4  # type: ignore

MUTATION_FACTOR = 2.0
POPULATION_SIZE = 100

ELITE_COUNT = 5
MAX_ITERATIONS = MAX_FUNCTION_EVALUATIONS // POPULATION_SIZE - 1

POPULATION = [[random() * 200 - 100 for _ in range(2)]
              for _ in range(POPULATION_SIZE)]


def main():

    print(
        evolve(
            FUNCTION,  # type: ignore
            POPULATION,
            MUTATION_FACTOR,
            POPULATION_SIZE,
            ELITE_COUNT,
            MAX_ITERATIONS
        )
    )

    plot_contour_chart_2d(FUNCTION, MAX_BOUND)  # type: ignore
    plt.show()


if __name__ == '__main__':
    RED = Color("red")  # type: ignore
    GREEN = Color("green")  # type: ignore
    BLUE = Color("blue")  # type: ignore
    COLORS = list(BLUE.range_to(GREEN, MAX_ITERATIONS // 2))  # type: ignore
    COLORS += list(  # type: ignore
        GREEN.range_to(  # type: ignore
            RED,
            MAX_ITERATIONS - MAX_ITERATIONS // 2
        )
    )

    main()
