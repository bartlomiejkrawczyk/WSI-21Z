from enum import IntEnum
from array import array
from random import choice
from typing import Callable, List, Dict, Tuple
import os
import time


class Field(IntEnum):
    START = ord("S")
    FROZEN = ord("F")
    HOLE = ord("H")
    GOAL = ord("G")


class Action(IntEnum):
    LEFT = 0
    DOWN = 1
    RIGHT = 2
    UP = 3


def reward_default(field: Field) -> float:
    if field == Field.GOAL:
        return 1.0
    return 0.0


def reward_2(field: Field) -> float:
    if field == Field.GOAL:
        return 1.0
    elif field == Field.HOLE:
        return -1.0
    return 0.0


def reward_3(field: Field) -> float:
    if field == Field.GOAL:
        return 10.0
    elif field == Field.HOLE:
        return -1.0
    return 0.0


REWARD_FUNCTIONS = [reward_default, reward_2, reward_3]


class FrozenLake:
    """
    Winter is here. You and your friends were tossing around a frisbee at the
    park when you made a wild throw that left the frisbee out in the middle of
    the lake. The water is mostly frozen, but there are a few holes where the
    ice has melted. If you step into one of those holes, you'll fall into the
    freezing water. At this time, there's an international frisbee shortage, so
    it's absolutely imperative that you navigate across the lake and retrieve
    the disc. However, the ice is slippery, so you won't always move in the
    direction you intend.
    The surface is described using a grid like the following
        SFFF
        FHFH
        FFFH
        HFFG
    S : starting point, safe
    F : frozen surface, safe
    H : hole, fall to your doom
    G : goal, where the frisbee is located
    The episode ends when you reach the goal or fall in a hole.
    You receive a reward of 1 if you reach the goal, and zero otherwise.
    """

    def __init__(self, reward_function: Callable[[Field], float]) -> None:
        self.map = array("b",
                         b"SFFFFFFF"
                         b"FFFFFFFF"
                         b"FFFHFFFF"
                         b"FFFFFHFF"
                         b"FFFHFFFF"
                         b"FHHFFFHF"
                         b"FHFFHFHF"
                         b"FFFHFFFG")
        self.length = 8
        self.reward_function = reward_function
        self.state = 0

        self.possible_results: Dict[int, Dict[Action,
                                              List[Tuple[int, float, bool]]]] = {}

        for row in range(self.length):
            for col in range(self.length):
                state = row * self.length + col
                field = Field(self.map[state])
                self.possible_results[state] = {}

                for action in Action:
                    results: List[Tuple[int, float, bool]] = []

                    if field == Field.GOAL or field == Field.HOLE:
                        results.append((state, 0.0, True))
                    else:
                        results.append(
                            self.move_result(
                                row, col, Action((action - 1) % 4)))

                        results.append(
                            self.move_result(row, col, action))

                        results.append(
                            self.move_result(
                                row, col, Action((action + 1) % 4)))

                    self.possible_results[state][action] = results

    def increment(self, row: int, col: int, action: Action):
        if action == Action.LEFT:
            col = max(col - 1, 0)
        elif action == Action.DOWN:
            row = min(row + 1, self.length - 1)
        elif action == Action.RIGHT:
            col = min(col + 1, self.length - 1)
        elif action == Action.UP:
            row = max(row - 1, 0)
        return (row, col)

    def move_result(self, row: int, col: int, action: Action) -> Tuple[int, float, bool]:
        new_row, new_col = self.increment(row, col, action)
        new_state = new_row * self.length + new_col
        new_field = Field(self.map[new_state])

        return (
            new_state,
            self.reward_function(new_field),
            new_field == Field.GOAL or new_field == Field.HOLE,
        )

    def step(self, action: Action) -> Tuple[int, float, bool]:
        result = choice(self.possible_results[self.state][action])
        self.state = result[0]
        self.last_action = action
        return result

    def reset(self):
        self.state = 0

    def render(self):
        map = [
            [
                chr(self.map[row * self.length + col])
                for col in range(self.length)
            ]
            for row in range(self.length)
        ]

        map[self.state // self.length][self.state % self.length] = (
            map[self.state // self.length][self.state % self.length].lower()
        )

        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

        print("\n")
        if self.last_action is not None:
            print(
                f"  ({['Left', 'Down', 'Right', 'Up'][self.last_action]})\n")
        else:
            print("\n")

        for row in map:
            print("".join(row))

        time.sleep(0.2)
