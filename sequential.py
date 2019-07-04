# A simple program demonstrating a parallel python program which determines
# how many numbers fall within a user-specified range

import numpy as np
import time

# Initialize random number generator with a seed value
np.random.RandomState(999)

# Generate an array of random number between 0 and 10
numberArray = np.random.randint(0, 10, size=[10000, 10000])
data = numberArray.tolist()

# A function that counts how many elements fall between a range of values
# given a one-dimensional array
def range_count(row, minimum=2, maximum=5):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

# An array to store how many values fall between each record in our array
# of values
results = []

# Track the start time of the program
startTime = time.time()

# Iterate through each row in the 2D array of values and determine how many times
# each of the values fall between our range of specified values
for row in data:
    results.append(range_count(row, minimum=2, maximum=5))

# Determine the execution time of the program
totalTime = time.time() - startTime

print("Sequential execution completed in %s seconds." % (totalTime))

# Print results from the first 5 rows
print(results[:5])
