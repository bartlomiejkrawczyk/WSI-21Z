from evolutionary_algorithm import evolve
from cec2017.functions import f4
import numpy as np
from itertools import product
import csv
from statistics import stdev
from typing import Any, List

MAX_BOUND = 100
FUNCTION = f4

MUTATION_FACTORS = [0.1, 1.0, 10.0, 50.0]
ELITE_COUNTS = [1, 5, 10]
POPULATION_SIZES = [10, 50, 100]

MUTATION_PROBABILITY = 0.20
MAX_FUNCTION_EVALUATIONS = 10_000


def test_algorithm() -> None:
    with open('02-evolutionary_algorithm/values.csv', 'w') as handle:
        writer = csv.writer(handle)
        writer.writerow(['index', 'mutation_factor',
                        'elite_count', 'population_size', 'value', 'point'])
        for i, mutation_factor, elite_count, population_size in product(range(25), MUTATION_FACTORS, ELITE_COUNTS, POPULATION_SIZES):
            population = [list(np.random.uniform(-MAX_BOUND, MAX_BOUND, size=2))
                          for _ in range(population_size)]
            max_iterations = MAX_FUNCTION_EVALUATIONS // population_size - 1
            point, value = evolve(FUNCTION, population, mutation_factor,
                                  population_size, MUTATION_PROBABILITY, elite_count, max_iterations)

            writer.writerow([i, mutation_factor, elite_count,
                            population_size, value, point])
            print(value, point)


def generate_table_with_comparison(column: str, current: Any) -> None:
    values = []

    with open('02-evolutionary_algorithm/values.csv', 'r') as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            i, mutation_factor, elite_count, population_size, value, point = row.values()
            i = int(i)
            mutation_factor = float(mutation_factor)
            elite_count = int(elite_count)
            population_size = int(population_size)
            value = float(value)

            if column == 'mutation_factor' and mutation_factor == current:
                values.append(value)
            elif column == 'elite_count' and elite_count == current:
                values.append(value)
            elif column == 'population_size' and population_size == current:
                values.append(value)

    print(column, '=', current, min(values), sum(values) /
          len(values), stdev(values),  max(values), sep='\t')


def print_table(column: str, values: List[Any]) -> None:
    print('Type     ', '=   ', 'Value', 'Min             ',
          'Average          ', 'Std             ', 'Max         ', sep='\t')
    for value in values:
        generate_table_with_comparison(column, value)

    print()


def print_tables() -> None:
    print_table('mutation_factor', MUTATION_FACTORS)
    print_table('elite_count', ELITE_COUNTS)
    print_table('population_size', POPULATION_SIZES)


def main():
    # test_algorithm()
    print_tables()


if __name__ == '__main__':
    main()
