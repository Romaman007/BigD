from timeit import default_timer
from contextlib import contextmanager
import numpy as np
import os

@contextmanager
def temp_file(f_name: str, size_in_Gb: int = 2):
    arr = np.random.randint(low=2**31,high=None,size=2**34*size_in_Gb//2**5)
    try:
        with open(f_name, "wb") as f:
            f.write(arr.data)
        yield f_name
    finally:
        os.remove(f_name)

@contextmanager
def timer():
    start = default_timer()
    yield
    end = default_timer()
    print(f"Time: {end - start}")
    return end - start