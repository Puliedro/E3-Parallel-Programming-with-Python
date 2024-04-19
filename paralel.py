import math
from multiprocessing import Pool
import time

def f(x):
    return math.sqrt(1 - x**2)

def partial_sum(start_end):
    start, end, dx = start_end
    return sum(f(i * dx) * dx for i in range(start, end))

def compute_area_parallel(N, num_processes):
    dx = 1.0 / N
    intervals = [(i * N // num_processes, (i + 1) * N // num_processes, dx) for i in range(num_processes)]

    # Start timing here
    start_time = time.time()

    with Pool(num_processes) as pool:
        result = sum(pool.map(partial_sum, intervals))

    # Calculate total computation time
    total_computation_time = time.time() - start_time

    # The result is scaled by 4 as it seems to be calculating an area under a quarter circle
    result *= 4
    print(f"Computed Area for n = {N} and {num_processes} processes: {result}")
    print(f"Elapsed time for n = {N} and {num_processes} processes: {total_computation_time} seconds\n")
    return result

if __name__ == "__main__":
    n = [100000, 1000000, 10000000]
    m = [4, 8, 12]
    for y in m:
        for x in n:
            compute_area_parallel(x,y) 



