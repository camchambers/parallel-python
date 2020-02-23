# A simple program that iterates through a two-dimensional array and determines how
# many values within each row fall within a user-defined range.
# This example serves as a baseline for demonstrating the speedup 
# of a a parallel version.

import numpy as np
import time

# A function that counts how many elements fall between a range of values
# given a one-dimensional array
def range_count(row, minimum, maximum):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

# Initialize random number generator with a seed value
np.random.RandomState(999)

# Generate a two-dimensional 10,000 x 10,000 array of random
# numbers falling between 0 and 10
numberArray = np.random.randint(0, 10, size=[10000, 10000])
data = numberArray.tolist()

# An array to store how many values fall between each record in our array
# of values
results = []

# Track the start time of the program
startTime = time.time()

# Iterate through each row in the two-dimensional array of results 
# and determine how many times each of the values fall between
# the user-defined range of values
for row in data:
    results.append(range_count(row, minimum=2, maximum=5))

# Determine the execution time of the program
totalTime = time.time() - startTime

print("Sequential execution completed in %s seconds." % (totalTime))