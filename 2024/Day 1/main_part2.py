import numpy as np
from collections import Counter

pairs = np.genfromtxt('./input.txt', delimiter='   ', skip_header=0, dtype=int)
left = pairs[:,0]
right = pairs[:,1]
counts = Counter(right)
print(sum([i * counts[i] for i in left]))