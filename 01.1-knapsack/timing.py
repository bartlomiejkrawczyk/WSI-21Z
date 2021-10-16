from random import randint, seed
import time
from knapsack_problem import backpack_problem_comprehensive


def time_it(N: int):
    seed(1)
    w = [randint(1, 10) for _ in range(N)]  # waga przedmiotów
    W = 9  # maksymalna waga plecaka
    p = [randint(1, 10) for _ in range(N)]  # wartość przedmiotów

    start_time = time.time()
    print(backpack_problem_comprehensive(w, W, p))
    print(f"For {N} items it took {time.time() - start_time} seconds")


if __name__ == '__main__':
    time_it(24)
