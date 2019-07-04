# Display the number of processors available on the current machine

import multiprocessing as mp
print("Number of processors: ", mp.cpu_count())