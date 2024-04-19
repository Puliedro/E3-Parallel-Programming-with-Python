import math
import time

def f(x):
    return math.sqrt(1 - x ** 2) # Formula

def compute_area(N):
    dx = 1.0 / N # Dx value
    
    start_time = time.time() # Profiling start
    total_sum = sum(f(i * dx) * dx for i in range(N)) # Making the sum
    
    # The sum calculates 1/4th of the circle, multiply by 4 to get full area
    result = 4 * total_sum 
    
    elapsed_time = time.time() - start_time # Profiling end
    print(f"Computed Area for n = {N}: {result}")
    print(f"Elapsed time for n = {N}: {elapsed_time} seconds\n")
    
    return result

if __name__ == "__main__":
    n = [100000, 1000000, 10000000]
    for x in n:
        compute_area(x) 

