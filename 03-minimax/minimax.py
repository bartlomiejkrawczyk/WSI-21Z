from checkers import Board, Game, Player, EVALUATION_FUNCTION
from math import inf
from random import randint


def evaluate_random(board: Board) -> float:
    return randint(-100, 100)


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

    if board.blue == 0:
        return -inf
    elif board.white == 0:
        return inf

    evaluation -= 2 * ((b_max_x - b_min_x) * (b_max_y - b_min_y)) / board.blue
    evaluation += 2 * ((w_max_x - w_min_x) * (w_max_y - w_min_y)) / board.white

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
                evaluation -= 5 + (board.size - pawn.y)

    return evaluation


def minimax_full(
        board: Board,
        depth: int,
        evaluation_function: EVALUATION_FUNCTION) -> float:

    moves = board.all_possible_moves()

    if len(moves) == 0:
        if board.player == Player.BLUE:
            return -inf
        else:
            return inf
    elif depth == 0:
        return evaluation_function(board)

    evaluation = [minimax_full(board.copy_and_perform_move(
        move), depth - 1, evaluation_function) for move in moves]

    if board.player == Player.BLUE:
        return max(evaluation)
    else:
        return min(evaluation)


def minimax_a_b(
        board: Board,
        depth: int,
        evaluation_function: EVALUATION_FUNCTION,
        alpha: float = -inf,
        beta: float = inf) -> float:

    moves = board.all_possible_moves()

    if len(moves) == 0:
        if board.player == Player.BLUE:
            return -inf
        else:
            return inf
    elif depth == 0:
        return evaluation_function(board)

    if board.player == Player.BLUE:
        for move in moves:
            new_board = board.copy_and_perform_move(move)
            alpha = max(
                alpha,
                minimax_a_b(new_board,
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
                minimax_a_b(new_board,
                            depth - 1,
                            evaluation_function,
                            alpha, beta)
            )
            if alpha >= beta:
                return alpha
        return beta


def main() -> None:
    Game.player_contra_ai(evaluate_basic, minimax_a_b)
    # Game.ai_contra_ai_with_display(evaluate_basic, evaluate_basic,
    #                                minimax_a_b, minimax_a_b, 5, 5)
    # Game.ai_contra_ai(evaluate_basic, evaluate_basic,
    #                   minimax_a_b, minimax_a_b, 1, 4)


if __name__ == '__main__':
    main()
