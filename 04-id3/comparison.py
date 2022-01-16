from random import randint, shuffle, seed
from reader import read_file
from id3 import run_id3
from statistics import mean, stdev
from itertools import product
from typing import Tuple, List

import multiprocessing.pool


def test_tree(args: Tuple[str, int, int]) -> Tuple[List[List[int]], List[str]]:
    file, class_column, seed_val = args
    seed(seed_val)
    data = read_file(file, class_column)
    shuffle(data)
    training_data_size = 3 * len(data) // 5
    training_data = data[: training_data_size]
    testing_data = data[training_data_size:]

    tree = run_id3(training_data)

    classes: List[str] = []

    result: List[List[int]] = []

    for tested in testing_data:
        predicted = tree.identify(tested.values)
        expected = tested.expected_class
        if not predicted in classes:
            classes.append(predicted)
            result.append([0] * len(result))

            for row in result:
                row.append(0)

        if not expected in classes:
            classes.append(expected)
            result.append([0] * len(result))

            for row in result:
                row.append(0)

        result[classes.index(expected)][classes.index(predicted)] += 1

    return result, classes


def format_table(result: List[List[int]], classes: List[str]) -> str:
    str_result = 'expected / predicted |'

    for class_ in classes:
        str_result += f'{class_}|'
    str_result = str_result[:-1]
    str_result += '\n'

    str_result += '-|' * (len(classes) + 1)
    str_result = str_result[:-1]
    str_result += '\n'

    for x, row in enumerate(result):
        str_result += f'{classes[x]}|'
        for count in row:
            str_result += f'{count}|'
        str_result = str_result[:-1]
        str_result += '\n'

    return str_result


def get_correct(result: List[List[int]]) -> float:
    total = 0
    for row in result:
        total += sum(row)

    correct = 0
    for x in range(len(result)):
        correct += result[x][x]

    return correct / total


FUNCTIONS = [
    min,
    mean,
    max,
    stdev
]


class Result:
    def __init__(self, name: str, file: str, class_column: int = 0) -> None:
        self.name = name
        with multiprocessing.pool.Pool() as pool:
            seed(13208731)
            self.results = pool.map(
                test_tree, product([file], [class_column], [
                                   randint(0, 10000000) for _ in range(25)])
            )

            self.percentages = [get_correct(result[0]) * 100
                                for result in self.results]

    def str_results(self) -> str:
        result = ''
        for res in self.results:
            result += format_table(res[0], res[1])
            result += '\n'
        return(result)

    def __str__(self) -> str:
        result = f'{self.name} |'
        for func in FUNCTIONS:
            result += f'{func(self.percentages)} % |'
        result = result[:-1]

        return result


def print_divider():
    result = 'name |'
    divider = '-|'
    for func in FUNCTIONS:
        result += f'{func.__name__} |'
        divider += '-|'
    result = result[:-1]
    divider = divider[:-1]
    print(result)
    print(divider)


FILES = {
    'Agaricus Lepiota': ('04-id3/data/agaricus-lepiota.data', 0),
    'Breast Cancer': ('04-id3/data/breast-cancer.data', 0),
    'Car': ('04-id3/data/car.data', 6),
    'Tic-Tac-Toe': ('04-id3/data/tic-tac-toe.data', 9),
    'Ache': ('07-bayesian-network/data/ache.data', 3)
}


def main():
    results = [Result(name, args[0], args[1]) for name, args in FILES.items()]

    for result in results:
        print(result.str_results())

    print_divider()
    for result in results:
        print(result)


if __name__ == '__main__':
    main()
