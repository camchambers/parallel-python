# A simple program that iterates through a two-dimensional array and determines how
# many values within each row fall within a user-defined range.
# This example is a parallel version of the sequential.py program.

import numpy as np
import time
import multiprocessing as mp
import argparse

# A function that counts how many elements fall between a range of values
# given a one-dimensional array
def range_count(row, minimum=2, maximum=5):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

# Parse program arguments
parser = argparse.ArgumentParser()
parser.add_argument('--cpus', nargs='?', const=mp.cpu_count(), type=int)
args = parser.parse_args()

# Number of CPUs to use based on cpu argument (defaults to available CPUs)
cpuCount = mp.cpu_count() if args.cpus == None else args.cpus

# Default to the maximum number of cpus if argument is great than the number available
cpuCount = mp.cpu_count() if cpuCount > mp.cpu_count() else cpuCount

# Display the number of processors used for processing
print("Using {} CPU(s)".format(cpuCount))

# Initialize random number generator with a seed value
np.random.RandomState(999)

# Generate an array of random number between 0 and 10
numberArray = np.random.randint(0, 10, size=[15000, 15000])
data = numberArray.tolist()

# Track the start time of the program
startTime = time.time()

# Create a pool of processors
pool = mp.Pool(cpuCount)

results = pool.map(range_count, [row for row in data])

# Close the pool of processors
pool.close()    

# Determine the execution time of the program
totalTime = time.time() - startTime

print("Parallel execution completed in %s seconds." % (totalTime))