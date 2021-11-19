from checkers import Board, Game, Player, EVALUATION_FUNCTION
from math import inf
from itertools import product
from typing import List, Tuple

import multiprocessing.pool


def evaluate_basic(board: Board) -> float:
    evaluation: float = 0
    pawns = board.get_pawns()

    for pawn in pawns:
        if pawn.player == Player.BLUE:
            if pawn.king:
                evaluation += 10
            else:
                evaluation += 1
        else:
            if pawn.king:
                evaluation -= 10
            else:
                evaluation -= 1

    return evaluation


def evaluate_version_1(board: Board) -> float:
    evaluation: float = 0
    pawns = board.get_pawns()

    b_max_x = 0
    b_min_x = board.size
    b_max_y = 0
    b_min_y = board.size

    w_max_x = 0
    w_min_x = board.size
    w_max_y = 0
    w_min_y = board.size

    for pawn in pawns:

        if pawn.player == Player.BLUE:

            b_max_x = max(b_max_x, pawn.x)
            b_min_x = min(b_min_x, pawn.x)
            b_max_y = max(b_max_y, pawn.y)
            b_min_y = min(b_min_y, pawn.y)

            if pawn.king:
                evaluation += 10
            else:
                evaluation += 1
        else:

            w_max_x = max(w_max_x, pawn.x)
            w_min_x = min(w_min_x, pawn.x)
            w_max_y = max(w_max_y, pawn.y)
            w_min_y = min(w_min_y, pawn.y)

            if pawn.king:
                evaluation -= 10
            else:
                evaluation -= 1

    evaluation -= (b_max_x - b_min_x) * (b_max_y - b_min_y)
    evaluation += (w_max_x - w_min_x) * (w_max_y - w_min_y)

    return evaluation


def evaluate_version_2(board: Board) -> float:
    evaluation: float = 0
    pawns = board.get_pawns()

    for pawn in pawns:
        if pawn.player == Player.BLUE:
            if pawn.king:
                evaluation += 10
            else:
                if pawn.y < board.size / 2:
                    evaluation += 5
                else:
                    evaluation += 7
        else:
            if pawn.king:
                evaluation -= 10
            else:
                if pawn.y > board.size / 2:
                    evaluation -= 5
                else:
                    evaluation -= 7

    return evaluation


def evaluate_version_3(board: Board) -> float:
    evaluation: float = 0
    pawns = board.get_pawns()

    for pawn in pawns:
        if pawn.player == Player.BLUE:
            if pawn.king:
                evaluation += 10
            else:
                evaluation += 5 + pawn.y
        else:
            if pawn.king:
                evaluation -= 10
            else:
                evaluation -= 5 - (board.size - pawn.y)

    return evaluation


def minimax_full(
        board: Board,
        depth: int,
        evaluation_function: EVALUATION_FUNCTION) -> float:

    moves = board.all_possible_moves()

    if len(moves) == 0 or depth == 0:
        return evaluation_function(board)

    evaluation = [minimax_full(board.copy_and_perform_move(
        move), depth - 1, evaluation_function) for move in moves]

    if board.player == Player.BLUE:
        return max(evaluation)
    else:
        return min(evaluation)


def minimax_a_b_recurr(
        board: Board,
        depth: int,
        evaluation_function: EVALUATION_FUNCTION,
        alpha: float = -inf,
        beta: float = inf) -> float:

    moves = board.all_possible_moves()

    if len(moves) == 0 or depth == 0:
        return evaluation_function(board)

    if board.player == Player.BLUE:
        for move in moves:
            new_board = board.copy_and_perform_move(move)
            alpha = max(
                alpha,
                minimax_a_b_recurr(new_board,
                                   depth - 1,
                                   evaluation_function,
                                   alpha, beta)
            )
            if alpha >= beta:
                return beta
        return alpha
    else:
        for move in moves:
            new_board = board.copy_and_perform_move(move)
            beta = min(
                beta,
                minimax_a_b_recurr(new_board,
                                   depth - 1,
                                   evaluation_function,
                                   alpha, beta)
            )
            if alpha >= beta:
                return alpha
        return beta


PLAYER = [
    Player.WHITE,
    Player.BLUE
]

DEPTHS = [
    1, 2, 3, 4, 5
]

EVALUATION_FUNCTIONS = [
    evaluate_basic,
    evaluate_version_1,
    evaluate_version_2,
    evaluate_version_3
]

EVALUATION_FUNCTIONS_NAMES = [
    evaluate_basic.__name__,
    evaluate_version_1.__name__,
    evaluate_version_2.__name__,
    evaluate_version_3.__name__
]


def run_ai_tuple(tuple: Tuple[EVALUATION_FUNCTION, int, Player]):
    eval, depth, player = tuple
    if player == Player.WHITE:
        result = Game.ai_contra_ai(
            eval, evaluate_basic,
            minimax_a_b_recurr, minimax_a_b_recurr,
            depth, 3
        )
    else:
        result = Game.ai_contra_ai(
            evaluate_basic, eval,
            minimax_a_b_recurr, minimax_a_b_recurr,
            3, depth
        )
    line = f'{player},{eval.__name__},{depth},{result}\n'
    print(line)
    return line


def run_ai(eval: EVALUATION_FUNCTION, depth: int, player: Player):
    if player == Player.WHITE:
        return Game.ai_contra_ai(
            eval, evaluate_basic,
            minimax_a_b_recurr, minimax_a_b_recurr,
            depth, 3
        )
    return Game.ai_contra_ai(
        evaluate_basic, eval,
        minimax_a_b_recurr, minimax_a_b_recurr,
        3, depth
    )


def test_ai() -> None:
    with multiprocessing.pool.Pool() as pool:
        results = pool.map(
            run_ai_tuple,
            product(
                EVALUATION_FUNCTIONS,
                DEPTHS,
                PLAYER
            )
        )
    with open('03-minimax/result/score.csv', 'w') as handle:
        handle.writelines(results)


def format_list(player: List[List[List[int]]]) -> None:
    line = 'evaluation \\ depth|'
    line2 = '-|'
    for d in DEPTHS:
        line += f'{d}|'
        line2 += '-|'
    print(line[:-1])
    print(line2[:-1])

    values = ['win', 'draw', 'lose']

    for i, row in enumerate(player):
        line = EVALUATION_FUNCTIONS_NAMES[i] + '|'
        for x in row:
            for val, res in zip(x, values):
                if val == 1:
                    line += f'{res}|'
        print(line[:-1])
    print()


def format_result() -> None:
    player_1 = [[[0 for _ in range(3)] for _ in DEPTHS]
                for _ in EVALUATION_FUNCTIONS]
    player_2 = [[[0 for _ in range(3)] for _ in DEPTHS]
                for _ in EVALUATION_FUNCTIONS]
    with open('03-minimax/result/score.csv', 'r') as handle:
        for line in handle.readlines():
            line = line.rstrip()
            line = line.split(',')
            player = line[0]
            eval = line[1]
            depth = int(line[2])
            result = line[3]
            if player == 'Player.WHITE':
                if result == 'Player.WHITE':
                    player_1[EVALUATION_FUNCTIONS_NAMES.index(
                        eval)][DEPTHS.index(int(depth))][0] += 1
                elif result == 'None':
                    player_1[EVALUATION_FUNCTIONS_NAMES.index(
                        eval)][DEPTHS.index(int(depth))][1] += 1
                else:
                    player_1[EVALUATION_FUNCTIONS_NAMES.index(
                        eval)][DEPTHS.index(int(depth))][2] += 1
            else:
                if result == 'Player.BLUE':
                    player_2[EVALUATION_FUNCTIONS_NAMES.index(
                        eval)][DEPTHS.index(int(depth))][0] += 1
                elif result == 'None':
                    player_2[EVALUATION_FUNCTIONS_NAMES.index(
                        eval)][DEPTHS.index(int(depth))][1] += 1
                else:
                    player_2[EVALUATION_FUNCTIONS_NAMES.index(
                        eval)][DEPTHS.index(int(depth))][2] += 1
    format_list(player_1)
    format_list(player_2)


def main() -> None:
    # Game.player_contra_ai(evaluate_basic, minimax_full)
    # Game.ai_contra_ai_with_display(evaluate_basic, evaluate_version_1,
    #                                minimax_a_b_recurr, minimax_full, 5, 1)
    # print(Game.ai_contra_ai(evaluate_basic, evaluate_basic,
    #                         minimax_a_b_recurr, minimax_full, 5, 5))
    test_ai()
    # format_result()


if __name__ == '__main__':
    main()
