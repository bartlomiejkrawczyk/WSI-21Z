import numpy as np
from typing import List, Tuple


def backpack_problem_comprehensive(weights: List[int], max_weight: int, values: List[int]) -> Tuple[List[int], int]:
    max_value = 0
    backpack = [0] * len(weights)
    for i in range(2 ** len(weights)):
        value = 0
        weight = 0
        binary = bin(i)[2:]
        binary = [0] * (len(weights) - len(binary)) + \
            [int(digit) for digit in binary]
        for j, n in enumerate(binary):
            if n == 1:
                weight += weights[j]
                value += values[j]
        if weight <= max_weight:
            if max_value < value:
                max_value = value
                backpack = binary
    return backpack, max_value


def backpack_problem_heuristics(weights: List[int], max_weight: int, values: List[int]) -> Tuple[List[int], int]:
    value_to_weight = [p/w for p, w in zip(values, weights)]
    value_to_weight, weights, values, indexes = zip(
        *sorted(zip(value_to_weight, weights, values, range(len(weights))), reverse=True))
    backpack_value = 0
    backpack_weight = 0
    backpack = [0] * len(weights)
    for weight, value, i in zip(weights, values, indexes):
        if weight + backpack_weight <= max_weight:
            backpack[i] = 1
            backpack_value += value
            backpack_weight += weight
    return backpack, backpack_value


def format_solution(result: Tuple[List[int], int]) -> str:
    return f'Total value: {result[1]}\nChoosen items: {[i for i, digit in enumerate(result[0], 1) if digit == 1]}'


def main():
    w = np.array([8, 3, 5, 2])  # waga przedmiotów
    W = 9  # maksymalna waga plecaka
    p = np.array([16, 8, 9, 6])  # wartość przedmiotów

    results = [backpack_problem_comprehensive(
        w, W, p), backpack_problem_heuristics(w, W, p)]

    for r in results:
        print(format_solution(r), '\n')


if __name__ == '__main__':
    main()
