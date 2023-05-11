import numpy as np
import mmap
import multiprocessing
from func import timer,temp_file


def get_all(arr: np.array, x: int):
    sum_of_arr =2**32
    min=2**32
    max=0
    for i in arr:
        sum_of_arr += i
        if i < min:
            min = i
        if i > max:
            max = i
    return [sum_of_arr,min,max]

def mmap_reading():
    with timer():
        with temp_file('hello.txt') as file:
            with open(file, 'r+b') as f:
                with mmap.mmap(f.fileno(), offset=0, length=0, access=mmap.ACCESS_WRITE) as mm:
                    arr = np.frombuffer(mm,dtype=np.int32)
                    print(f'File weight: {arr.itemsize*arr.size//1024//1024} Mb')
                    n_proc = multiprocessing.cpu_count()
                    arr = arr.reshape(n_proc,len(arr)//n_proc)
                    init = map(lambda x: (arr[x],x),range(n_proc))
                    with multiprocessing.Pool() as pool:
                        results=pool.starmap(get_all, init)
                    results = np.array(results,dtype=object)
                    print(f'Sum of arr: {sum(results[:,0]-2**32)}')
                    print(f'Min elem: {np.min(results[:,1])}')
                    print(f'Max elem: {np.max(results[:,2])}')
                    del arr


if __name__ == '__main__':
    mmap_reading()
