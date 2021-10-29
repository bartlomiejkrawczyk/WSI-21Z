import numpy as np
from typing import Callable, List, TYPE_CHECKING, Any, Tuple
from cec2017.functions import f4

if TYPE_CHECKING:
    NDArrayFloat = np.ndarray[Any, np.dtype[np.float]]
else:
    NDArrayFloat = Any

"""
Data:
    q(x) - function,
    P0 - starting_population,
    µ - population_size,
    σ - mutation_factor,
    pc - mutation_probability,
    tmax - max_iterations
Result:
    xˆ∗ - best_subject,
    oˆ∗ - best_rating

"""


def stop(iteration: int,
         max_iterations: int,
         population: List[NDArrayFloat],
         rating: List[float]) -> bool:
    if iteration >= max_iterations:
        return True
    return False


def reproduction(population: List[NDArrayFloat],
                 rating: List[float],
                 mutation_factor: float) -> List[NDArrayFloat]:
    pass


def genetic_operations(population: List[NDArrayFloat],
                       mutation_factor: float,
                       mutation_probability: float) -> List[NDArrayFloat]:
    pass


def succesion(population: List[NDArrayFloat],
              mutated: List[NDArrayFloat],
              rating: float,
              rating_mutated: float,
              elite_count: int) -> List[NDArrayFloat]:
    result = zip(*sorted(zip(rating + rating_mutated,
                 population + mutated), reverse=True))[1][:elite_count]


def evolve(function: Callable[[NDArrayFloat], float],
           population: List[NDArrayFloat],
           mutation_factor: float,
           population_size: int,
           mutation_probability: float,
           elite_count: int,
           max_iterations: int) -> Tuple[NDArrayFloat, float]:

    rating = [function(point) for point in population]
    best_rating, best_subject = min(zip(rating, population))
    pass

    t = 0
    # for _ in range(max_iterations):
    while not stop(t, max_iterations, population, rating):

        reproduced = reproduction(population, rating, population_size)

        mutated = genetic_operations(
            reproduced, mutation_factor, mutation_probability)

        rating_mutated = [function(point) for point in mutated]

        best_rating_mutated, best_subject_mutated = min(
            zip(rating_mutated, mutated))

        if best_rating >= best_rating_mutated:
            best_rating = best_rating_mutated
            best_subject = best_subject_mutated

        population = succesion(population, mutated, rating,
                               rating_mutated, elite_count)

        t += 1

    return best_subject, best_rating


def main():
    pass


if __name__ == '__main__':
    main()
