from random import shuffle
from reader import read_file
from id3 import run_id3
from statistics import mean, stdev
from itertools import product
from typing import Tuple

import multiprocessing.pool


def test_tree(args: Tuple[str, int]) -> float:
    file, class_column = args
    data = read_file(file, class_column)
    shuffle(data)
    training_data_size = len(data) // 5 * 3
    training_data = data[: training_data_size]
    testing_data = data[training_data_size:]

    tree = run_id3(training_data)

    correct = 0

    for tested in testing_data:
        if tree.get_class(tested.values) == tested.class_:
            correct += 1
    return correct / len(testing_data)


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
            self.results = pool.map(
                test_tree, product([file] * 25, [class_column])
            )

    def __str__(self) -> str:
        result = f'{self.name} |'
        for func in FUNCTIONS:
            result += f'{func(self.results)} |'
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
    'Agaricus Lepiota': '04-id3/data/agaricus-lepiota.data',
    'Breast Cancer': '04-id3/data/breast-cancer.data'
}


def main():
    print_divider()
    for name, file in FILES.items():
        print(Result(name, file))


if __name__ == '__main__':
    main()
