import numpy as np

pairs = np.genfromtxt('./input.txt', delimiter='   ', skip_header=0, dtype=int)
left = np.sort(pairs[:,0])
right = np.sort(pairs[:,1])
print(np.sum(np.abs(right - left)))