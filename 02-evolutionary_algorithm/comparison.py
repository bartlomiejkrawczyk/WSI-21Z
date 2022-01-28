from evolutionary_algorithm import evolve
from cec2017.functions import f4
import numpy as np
from itertools import product
from statistics import stdev, mean
from typing import List, Callable

MAX_BOUND = 100
FUNCTION: Callable[[List[float]], float] = f4  # type: ignore

MUTATION_FACTORS = [0.1, 1.0, 2.0, 3.0, 4.0,
                    5.0, 10.0, 20.0, 30.0, 40.0, 50.0, 100.0]
ELITE_COUNTS = [0, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50]
POPULATION_SIZES = [5, 10, 15, 20, 50, 100, 200, 1000]

MUTATION_PROBABILITY = 0.20
MAX_FUNCTION_EVALUATIONS = 10_000


def generate_table(column: str,
                   mutation_factor: List[float] = [1.0],
                   elite_count: List[int] = [5],
                   population_size: List[int] = [50]):
    print('| Type',
          '| Value',
          '| Min',
          '| Average',
          '| Std',
          '| Max |',
          sep='\t')

    for mutation, elite, population in product(mutation_factor, elite_count, population_size):
        values: List[float] = []
        for _ in range(25):
            values.append(
                evolve(
                    FUNCTION,  # type: ignore
                    [list(np.random.uniform(-MAX_BOUND, MAX_BOUND, size=10))
                     for _ in range(population)],
                    mutation,
                    population,
                    elite,
                    MAX_FUNCTION_EVALUATIONS // population - 1
                )[1]
            )

        if column == 'mutation_factor':
            print(column, mutation, min(values), mean(
                values), stdev(values),  max(values),  sep='|')
        elif column == 'elite_count':
            print(column, elite, min(values), mean(
                values), stdev(values),  max(values),  sep='|')
        elif column == 'population_size':
            print(column, population, min(values), mean(
                values), stdev(values),  max(values),  sep='|')
    print()


def main():
    generate_table('mutation_factor', mutation_factor=MUTATION_FACTORS)
    generate_table('elite_count', elite_count=ELITE_COUNTS)
    generate_table('population_size', population_size=POPULATION_SIZES)
    pass


if __name__ == '__main__':
    main()
