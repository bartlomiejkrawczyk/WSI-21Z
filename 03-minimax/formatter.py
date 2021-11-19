from comparison import DEPTHS, EVALUATION_FUNCTIONS, EVALUATION_FUNCTIONS_NAMES
from typing import List


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


def main() -> None:
    format_result()
    format_full_result()


if __name__ == '__main__':
    main()
