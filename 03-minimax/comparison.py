from checkers import Game, Player, EVALUATION_FUNCTION
from itertools import product
from typing import Tuple

import multiprocessing.pool

from minimax import (
    evaluate_random,
    evaluate_basic,
    evaluate_version_1,
    evaluate_version_2,
    evaluate_version_3,
    minimax_a_b
)


PLAYER = [
    Player.WHITE,
    Player.BLUE
]

DEPTHS = [
    1, 2, 3, 4, 5
]

EVALUATION_FUNCTIONS = [
    evaluate_random,
    evaluate_basic,
    evaluate_version_1,
    evaluate_version_2,
    evaluate_version_3
]

EVALUATION_FUNCTIONS_NAMES = [
    evaluate_random.__name__,
    evaluate_basic.__name__,
    evaluate_version_1.__name__,
    evaluate_version_2.__name__,
    evaluate_version_3.__name__
]


def run_ai(tuple: Tuple[EVALUATION_FUNCTION, int, Player]):
    eval, depth, player = tuple
    if player == Player.WHITE:
        result = Game.ai_contra_ai(
            eval, evaluate_basic,
            minimax_a_b, minimax_a_b,
            depth, 3
        )
    else:
        result = Game.ai_contra_ai(
            evaluate_basic, eval,
            minimax_a_b, minimax_a_b,
            3, depth
        )
    line = f'{player},{eval.__name__},{depth},{result}\n'
    print(line)
    return line


def test_ai() -> None:
    with multiprocessing.pool.Pool() as pool:
        results = pool.map(
            run_ai,
            product(
                EVALUATION_FUNCTIONS,
                DEPTHS,
                PLAYER
            )
        )
    with open('03-minimax/result/score.csv', 'w') as handle:
        handle.writelines(results)


def run_ai_full(tuple: Tuple[EVALUATION_FUNCTION, EVALUATION_FUNCTION, int, int, ]):
    eval1, eval2, depth1, depth2 = tuple
    result = Game.ai_contra_ai(
        eval1, eval2,
        minimax_a_b, minimax_a_b,
        depth1, depth2
    )
    line = f'{eval1.__name__},{eval2.__name__},{depth1},{depth2},{result}\n'
    print(line)
    return line


def test_ai_full() -> None:
    with multiprocessing.pool.Pool() as pool:
        results = pool.map(
            run_ai_full,
            product(
                EVALUATION_FUNCTIONS,
                EVALUATION_FUNCTIONS,
                DEPTHS,
                DEPTHS
            )
        )
    with open('03-minimax/result/full_score.csv', 'w') as handle:
        handle.writelines(results)


def run_ai_basic(tuple: Tuple[int, int]):
    depth1, depth2 = tuple
    result = Game.ai_contra_ai(
        evaluate_basic, evaluate_basic,
        minimax_a_b, minimax_a_b,
        depth1, depth2
    )
    line = f'{depth1},{depth2},{result}\n'
    print(line)
    return line


def test_ai_basic() -> None:
    with multiprocessing.pool.Pool() as pool:
        results = pool.map(
            run_ai_basic,
            product(
                DEPTHS,
                DEPTHS
            )
        )
    with open('03-minimax/result/basic_score.csv', 'w') as handle:
        handle.writelines(results)


def main():
    # test_ai()
    test_ai_full()
    # test_ai_basic()


if __name__ == '__main__':
    main()
