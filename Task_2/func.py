from timeit import default_timer
from contextlib import contextmanager
import numpy as np
import os


@contextmanager
def timer():
    start = default_timer()
    yield
    end = default_timer()
    print(f"Time: {end - start}")
    return end - start


def get_factors(num: int) -> int:
    factors = []
    divisor = 2
    sq = np.sqrt(num) + 1
    while (divisor <= sq):
        if num % divisor == 0:
            factors.append(divisor)
            num /= divisor
            sq = np.sqrt(num) + 1
        else:
            divisor += 1
    return len(factors) + 1


def get_sum_of_factors(g: list[int]) -> int:
    sum_of_factors = 0
    for i in g:
        sum_of_factors += get_factors(i)
    return sum_of_factors


def create_file(count: int) -> None:
    with open('file.txt', 'w') as f:
        for i in range(count):
            if i!= count-1:
                f.write(str(np.random.randint(low=2 ** 31, high=None)) + "\n")
            else:
                f.write(str(np.random.randint(low=2 ** 31, high=None)))


def get_data_from_file(filename: str) -> list[int]:
    with open(filename) as f:
        g = list(map(int, f.read().split('\n')))
    return g



if __name__ == '__main__':
    create_file(int(input()))
