from random import choice, uniform, shuffle
from statistics import stdev, mean
from typing import List, Callable

from frozenlake import Action, FrozenLake, REWARD_FUNCTIONS, Field
from multiprocessing.pool import Pool
from functools import partial
from itertools import repeat

MAX_STEPS = 400

LEARNING_RATE = 0.05

EPSILON = 0.1

GAMMA = 0.95


def q_learning(
        environment: FrozenLake,
        episodes: int,
        max_steps: int = MAX_STEPS,
        learning_rate: float = LEARNING_RATE,
        epsilon: float = EPSILON,
        gamma: float = GAMMA) -> List[List[float]]:

    qtable: List[List[float]] = [
        [0.0, 0.0, 0.0, 0.0]
        for _ in range(len(environment.map))
    ]

    for _ in range(episodes):
        environment.reset()

        for _ in range(max_steps):
            state = environment.state

            if uniform(0, 1) > epsilon:
                actions = list(Action)
                shuffle(actions)
                action = max(actions, key=lambda x: qtable[state][x])
            else:
                action = choice(tuple(Action))

            new_state, reward, done = environment.step(action)

            qtable[state][action] = (
                qtable[state][action]
                + learning_rate * (
                    reward
                    + gamma * max(qtable[new_state])
                    - qtable[state][action]
                )
            )

            if done:
                break

    return qtable


def evaluate_qtable(environment: FrozenLake, qtable: List[List[float]]) -> float:
    success_count = 0

    for _ in range(1000):
        environment.reset()

        for _ in range(200):
            state = environment.state
            action = max(Action, key=lambda x: qtable[state][x])
            _, _, done = environment.step(action)

            if done:
                success_count += (
                    Field(environment.map[environment.state]) == Field.GOAL
                )
                break

    return success_count / 10


def run_q_learning(episodes: int, reward: Callable[[Field], float]) -> float:
    environment = FrozenLake(reward)
    qtable = q_learning(environment, episodes)
    return evaluate_qtable(environment, qtable)


def render_frozenlake(environment: FrozenLake, qtable: List[List[float]]):
    for step in range(200):
        state = environment.state
        action = max(Action, key=lambda x: qtable[state][x])
        _, _, done = environment.step(action)

        environment.render()

        if done:
            print('Steps', step)
            break


def main():
    for reward in REWARD_FUNCTIONS:
        print(reward.__name__)
        print('episodes|min|avg|max|stdev')
        print('-|-' * 4)
        for episodes in [1000, 5000, 10_000, 25_000, 50_000, 100_000, 250_000]:
            with Pool() as pool:
                func = partial(run_q_learning, reward=reward)
                success_rate = pool.map(func, repeat(episodes, 25))
                print(
                    f'{episodes}|{min(success_rate)}|{mean(success_rate)}|{max(success_rate)}|{stdev(success_rate)}'
                )


def format_qtable(qtable: List[List[float]]):
    length = int(len(qtable) ** 0.5)

    for y in range(length):
        row = ''
        for x in range(length):
            row += max([('<', 0), ('V', 1), ('>', 2), ('^', 3)],
                       key=lambda val: qtable[y * length + x][val[1]])[0] + ' '
        print(row)


if __name__ == '__main__':
    main()

    environment = FrozenLake(REWARD_FUNCTIONS[1])
    qtable = q_learning(environment, 100_000)
    format_qtable(qtable)
    # print(qtable)
    # print(evaluate_qtable(environment, qtable))
    # environment.reset()

    # render_frozenlake(environment, qtable)
