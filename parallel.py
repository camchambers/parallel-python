# A simple program demonstrating a parallel python program which determines
# how many numbers fall within a user-specified range

import numpy as np
import time
import multiprocessing as mp

# Initialize random number generator with a seed value
np.random.RandomState(999)

# Generate an array of random number between 0 and 10
numberArray = np.random.randint(0, 10, size=[10000, 10000])
data = numberArray.tolist()

def range_count(row, minimum=2, maximum=5):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

# Track the start time of the program
startTime = time.time()

# Create a pool of processors
pool = mp.Pool(mp.cpu_count())

results = pool.map(range_count, [row for row in data])

# Step 3: Don't forget to close
pool.close()    

# Determine the execution time of the program
totalTime = time.time() - startTime

print("Parallel execution completed in %s seconds." % (totalTime))

# Print results from the first 5 rows
print(results[:5])
