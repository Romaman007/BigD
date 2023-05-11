import numpy as np

from func import timer,temp_file

def simple_reading():
    def get_max(arr: np.array):
        max=0
        for i in arr:
            if i>max:
                max=i
        print(f'Max elem: {max}')

    def get_min(arr: np.array):
        min=2**32
        for i in arr:
            if i<min:
                min=i
        print(f'Min elem: {min}')

    def get_sum(arr: np.array):
        sum=2**32
        for i in arr:
            sum+=i
        print(f'Sum of arr: {sum-2**32}')

    with timer():
        with temp_file('hello.txt') as file:
            with open(file,'r+b') as f:
                arr = np.frombuffer(f.read(),dtype=np.int32)
                print(f'File weight: {arr.itemsize*arr.size//1024//1024} Mb')
                get_sum(arr)
                get_min(arr)
                get_max(arr)


if __name__ == '__main__':
    simple_reading()
