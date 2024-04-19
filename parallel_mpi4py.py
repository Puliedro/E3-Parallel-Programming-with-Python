from mpi4py import MPI
import numpy as np
import math
import time

def f(x):
    return math.sqrt(1 - x**2)

def compute_area_mpi(N):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    dx = 1.0 / N
    local_n = N // size
    remainder = N % size

    if rank < remainder:
        local_n += 1
        local_start = rank * local_n
    else:
        local_start = rank * local_n + remainder

    local_end = local_start + local_n

    # Timing starts here
    start_time = time.time()

    local_sum = sum(f(i * dx) * dx for i in range(local_start, local_end))

    # Time after local computation
    local_computation_time = time.time() - start_time

    # Gather all local computation times at the root process for analysis
    all_computation_times = comm.gather(local_computation_time, root=0)

    # Reduce all local sums into a total sum at the root process
    total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

    # Total elapsed time for the root process
    if rank == 0:
        total_computation_time = time.time() - start_time
        result = 4 * total_sum
        print(f"Total Result = {N}: {result}")
        print(f"Total Computation Time for n = {N}: {total_computation_time} seconds")
        if all_computation_times:
            print("Computation times from all processes:", all_computation_times)
        return result

if __name__ == "__main__":
    n = [100000, 1000000, 10000000]
    for x in n:
        compute_area_mpi(x)




