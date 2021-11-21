from comparison import DEPTHS, EVALUATION_FUNCTIONS, EVALUATION_FUNCTIONS_NAMES
from typing import List, Union
from itertools import product


def format_list(player: List[List[List[int]]], text: bool = True) -> None:
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
            if text:
                for val, res in zip(x, values):
                    if val == 1:
                        line += f'{res}|'
            else:
                line += f'{x}|'
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


def format_full_result() -> None:
    player_1 = [[[0 for _ in range(3)] for _ in DEPTHS]
                for _ in EVALUATION_FUNCTIONS]
    player_2 = [[[0 for _ in range(3)] for _ in DEPTHS]
                for _ in EVALUATION_FUNCTIONS]
    with open('03-minimax/result/full_score.csv', 'r') as handle:
        for line in handle.readlines():
            line = line.rstrip()
            line = line.split(',')
            eval1 = line[0]
            eval2 = line[1]
            depth1 = int(line[2])
            depth2 = int(line[3])
            result = line[4]
            if result == 'Player.WHITE':
                player_1[EVALUATION_FUNCTIONS_NAMES.index(
                    eval1)][DEPTHS.index(int(depth1))][0] += 1
                player_2[EVALUATION_FUNCTIONS_NAMES.index(
                    eval2)][DEPTHS.index(int(depth2))][2] += 1
            elif result == 'Player.BLUE':
                player_1[EVALUATION_FUNCTIONS_NAMES.index(
                    eval1)][DEPTHS.index(int(depth1))][2] += 1
                player_2[EVALUATION_FUNCTIONS_NAMES.index(
                    eval2)][DEPTHS.index(int(depth2))][0] += 1
            else:
                player_1[EVALUATION_FUNCTIONS_NAMES.index(
                    eval1)][DEPTHS.index(int(depth1))][1] += 1
                player_2[EVALUATION_FUNCTIONS_NAMES.index(
                    eval2)][DEPTHS.index(int(depth2))][1] += 1

    format_list(player_1, False)
    format_list(player_2, False)


def check_missing_full():
    not_used: List[List[Union[str, int]]] = []
    with open('03-minimax/result/full_score.csv', 'r') as handle:
        lines = handle.readlines()
        for eval1, eval2, depth1, depth2 in product(
            EVALUATION_FUNCTIONS_NAMES,
            EVALUATION_FUNCTIONS_NAMES,
            DEPTHS,
            DEPTHS
        ):
            stripped: List[List[str]] = []
            for line in lines:
                stripped.append((line.split(',')[:-1]))
            there_is = False

            for s in stripped:
                if s[0] == eval1 and s[1] == eval2 and s[2] == str(depth1) and s[3] == str(depth2):
                    there_is = True
                    break
            if not there_is:
                not_used.append([eval1, eval2, depth1, depth2])
    print(not_used)


def format_game_result(game_result: List[List[List[int]]], text: bool = True) -> None:
    line = 'blue \\ white|'
    line2 = '-|'
    for d in DEPTHS:
        line += f'{d}|'
        line2 += '-|'
    print(line[:-1])
    print(line2[:-1])

    values = ['white', 'draw', 'blue']

    for i, row in enumerate(game_result):
        line = str(DEPTHS[i]) + '|'
        for x in row:
            if text:
                for val, res in zip(x, values):
                    if val == 1:
                        line += f'{res}|'
            else:
                line += f'{x}|'
        print(line[:-1])
    print()


def format_result_basic() -> None:
    game_result = [[[0 for _ in range(3)] for _ in DEPTHS]
                   for _ in EVALUATION_FUNCTIONS]
    with open('03-minimax/result/basic_score.csv', 'r') as handle:
        for line in handle.readlines():
            line = line.rstrip()
            line = line.split(',')
            depth1 = int(line[0])
            depth2 = int(line[1])
            result = line[2]
            if result == 'Player.WHITE':
                game_result[DEPTHS.index(int(depth2))
                            ][DEPTHS.index(int(depth1))][0] += 1
            elif result == 'None':
                game_result[DEPTHS.index(int(depth2))
                            ][DEPTHS.index(int(depth1))][1] += 1
            else:
                game_result[DEPTHS.index(int(depth2))
                            ][DEPTHS.index(int(depth1))][2] += 1
    format_game_result(game_result)


def main() -> None:
    # format_result()
    format_full_result()
    # check_missing_full()
    # format_result_basic()


if __name__ == '__main__':
    main()
