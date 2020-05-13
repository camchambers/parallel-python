# A simple program that iterates through a two-dimensional array and determines how
# many values within each row fall within a user-defined range.
# This example is a sequential version that explicitly uses 1 processor.

import numpy as np
import time
import multiprocessing as mp

# A function that counts how many elements fall between a range of values
# given a one-dimensional array
def range_count(row, minimum=2, maximum=5):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

# Display the number of processors available on the current machine
print("Using {} CPU(s)".format(1))

# Initialize random number generator with a seed value
np.random.RandomState(999)

# Generate an array of random number between 0 and 10
numberArray = np.random.randint(0, 10, size=[15000, 15000])
data = numberArray.tolist()

# Track the start time of the program
startTime = time.time()

# Create a pool of processors
pool = mp.Pool(1)

results = pool.map(range_count, [row for row in data])

# Close the pool of processors
pool.close()    

# Determine the execution time of the program
totalTime = time.time() - startTime

print("Sequential execution completed in %s seconds." % (totalTime))