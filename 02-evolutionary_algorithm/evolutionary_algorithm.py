import numpy as np
from typing import Callable, List, Tuple
from cec2017.functions import f4
from random import choices, gauss, random, sample
from plot_2d import plot_contour_chart_2d
from matplotlib import pyplot as plt
from colour import Color
import heapq


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


def stop(iteration: int,
         max_iterations: int,
         population: List[List[float]],
         rating: List[float]) -> bool:

    if iteration >= max_iterations:
        return True
    return False


def reproduction(population: List[List[float]],
                 rating: List[float],
                 population_size: int) -> List[List[float]]:
    """
    Tournament Selection

    From two points chosen at random the better one is chosen.
    """

    return [min(sample(list(zip(rating, population)), k=2))[1] for _ in range(population_size)]


def genetic_operations(population: List[List[float]],
                       mutation_factor: float) -> List[List[float]]:
    """
    Mutation

    For every point choose a random distance in every direction to move.
    Choose closer distance with greater probability.
    """

    return [[x + gauss(0, 1) * mutation_factor for x in subject] for subject in population]


def succesion(population: List[List[float]],
              mutated: List[List[float]],
              rating: List[float],
              rating_mutated: List[float],
              elite_count: int) -> List[List[float]]:
    """
    Elitary Succesion

    From previous population choose the best elite_count subjects.
    Append to them mutated subjects and remove excess (worst)
    individuals to match the population_size number.
    """

    zipped_population = heapq.nsmallest(elite_count, zip(rating, population))
    zipped_result = zipped_population + list(zip(rating_mutated, mutated))
    zipped_result = heapq.nsmallest(len(population), zipped_result)

    return [i[1] for i in zipped_result]


def evolve(function: Callable[[List[float]], float],
           population: List[List[float]],
           mutation_factor: float,
           population_size: int,
           elite_count: int,
           max_iterations: int) -> Tuple[List[float], float]:
    """Classical evolutionary algorithm"""

    rating = [function(point) for point in population]
    best_rating, best_subject = min(zip(rating, population))

    # t = 0
    # while not stop(t, max_iterations, population, rating):
    for t in range(max_iterations):

        if __name__ == '__main__':
            plt.scatter(*zip(*population), c=COLORS[t].get_hex(), marker='.')

        reproduced = reproduction(population, rating, population_size)

        mutated = genetic_operations(reproduced, mutation_factor)

        rating_mutated = [function(point) for point in mutated]

        best_rating_mutated, best_subject_mutated = min(
            zip(rating_mutated, mutated))

        if best_rating >= best_rating_mutated:
            best_rating = best_rating_mutated
            best_subject = best_subject_mutated

        population = succesion(population, mutated, rating,
                               rating_mutated, elite_count)

        # t += 1

    return best_subject, best_rating


MAX_FUNCTION_EVALUATIONS = 10_000

MAX_BOUND = 100
FUNCTION = f4

MUTATION_FACTOR = 2.0
POPULATION_SIZE = 20

ELITE_COUNT = 5
MAX_ITERATIONS = MAX_FUNCTION_EVALUATIONS // POPULATION_SIZE - 1

POPULATION = [list(np.random.uniform(-MAX_BOUND, MAX_BOUND, size=2))
              for _ in range(POPULATION_SIZE)]

RED = Color("red")
GREEN = Color("green")
BLUE = Color("blue")
COLORS = list(BLUE.range_to(GREEN, MAX_ITERATIONS // 2))
COLORS += list(GREEN.range_to(RED, MAX_ITERATIONS - MAX_ITERATIONS // 2))


def main():

    print(evolve(FUNCTION, POPULATION, MUTATION_FACTOR,
          POPULATION_SIZE, ELITE_COUNT, MAX_ITERATIONS))

    plot_contour_chart_2d(FUNCTION, MAX_BOUND)
    plt.show()


if __name__ == '__main__':
    main()
