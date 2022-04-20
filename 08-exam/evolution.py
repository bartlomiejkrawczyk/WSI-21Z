import random
from typing import Callable, List, Any
from random import choices
import heapq
from functools import total_ordering
from collections import Counter
from matplotlib import pyplot as plt

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
    def __init__(self, point: float) -> None:
        self.point = point

    def evaluate(self, function: Callable[[float], float]):
        self.rating = function(self.point)

    def __lt__(self, other: 'Point'):
        return self.rating < other.rating

    def __eq__(self, other: Any):
        return self.rating == other.rating

    def __str__(self) -> str:
        return str(self.point)

    def __hash__(self) -> int:
        return int(self.point)


def reproduction_proportional(population: List[Point],
                              population_size: int) -> List[Point]:
    return choices(
        population,
        weights=[p.rating for p in population],
        k=population_size)


def reproduction_proportional_quadratic(population: List[Point],
                                        population_size: int) -> List[Point]:
    return choices(
        population,
        weights=[(p.rating)**2 for p in population],
        k=population_size)


def reproduction_proportional_exponential(population: List[Point],
                                          population_size: int) -> List[Point]:
    return choices(
        population,
        weights=[1.5 ** (p.rating / 10) - 1 for p in population],
        k=population_size)


def reproduction_proportional_exponential_xd(population: List[Point],
                                             population_size: int) -> List[Point]:
    return choices(
        population,
        weights=[40 ** (p.rating / 10) - 1 for p in population],
        k=population_size)


def reproduction_tournamet_2(population: List[Point],
                             population_size: int) -> List[Point]:
    """
    Tournament Selection

    From two points chosen at random the better one is chosen.
    """

    return [
        max(
            choices(population, k=2)
        )
        for _ in range(population_size)]


def succesion_elitary_1(population: List[Point],
                        mutated: List[Point],
                        population_size: int) -> List[Point]:
    """
    Elitary Succesion

    From previous population choose the best elite_count subjects.
    Append to them mutated subjects and remove excess (worst)
    individuals to match the population_size number.
    """

    best_population = heapq.nlargest(1, population)

    return heapq.nlargest(population_size, best_population + mutated)


def succesion_generation(population: List[Point],
                         mutated: List[Point],
                         population_size: int) -> List[Point]:

    return mutated


def evolve(function: Callable[[float], float],
           starting_population: List[float],
           reproduction: Callable[[List[Point], int], List[Point]],
           succession: Callable[[List[Point], List[Point], int], List[Point]],
           max_iterations: int) -> List[int]:
    """
    Classical evolutionary algorithm

    without mutation and crossing
    """

    population = [Point(point) for point in starting_population]

    for p in population:
        p.evaluate(function)

    best = max(population)

    count = len(population)
    counts: List[int] = []

    for _ in range(max_iterations):
        count = len(Counter(population).values())
        counts.append(count)

        reproduced = reproduction(population, len(population))

        mutated = reproduced

        for p in mutated:
            p.evaluate(function)

        best_mutated = max(mutated)

        best = max(best, best_mutated)

        population = succession(population, mutated, len(population))

    return counts


def static(x: float) -> float:
    return 1.0


def linear(x: float) -> float:
    return x


def quadratic(x: float) -> float:
    return x**2


REPRODUCTIONS = [
    # reproduction_proportional_exponential,
    # reproduction_proportional_exponential,
    # reproduction_tournamet_2,

    # reproduction_proportional_exponential,
    # reproduction_proportional_exponential,
    # reproduction_tournamet_2,

    reproduction_proportional_exponential_xd,
    reproduction_proportional_exponential,
    reproduction_tournamet_2,
]

SUCCESSION = [
    # succesion_elitary_1,
    # succesion_elitary_1,
    # succesion_elitary_1,

    # succesion_generation,
    # succesion_generation,
    # succesion_generation,

    succesion_elitary_1,
    succesion_elitary_1,
    succesion_elitary_1,
]


FUNCTIONS: List[Callable[[float], float]] = [
    # static,
    # quadratic,
    # quadratic,

    # static,
    # quadratic,
    # quadratic,

    linear,
    static,
    linear,
]


POPULATION: List[float] = [float(i) for i in range(10)]

MAX_ITERATIONS = 16


def mutuj_os(osobnik: List[float], sila_mut: float):

    return [
        x + random.gauss(0, 1) * sila_mut
        for x in osobnik
    ]


def main():
    val: str = 'a'
    for function, reproduction, succesion in zip(FUNCTIONS, REPRODUCTIONS, SUCCESSION):
        counts = [0.0 for _ in range(MAX_ITERATIONS)]
        iterations = 100
        for _ in range(iterations):
            count = evolve(
                function,
                POPULATION,
                reproduction,
                succesion,
                MAX_ITERATIONS
            )
            for i, c in enumerate(count):
                counts[i] += c

        counts = [c / iterations for c in counts]

        plt.plot([i for i in range(len(counts))],
                 counts, label=f'{val}) {function.__name__}\n{reproduction.__name__}\n{succesion.__name__}')
        val = chr(ord(val) + 1)

        print()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
