import numpy as np
from itertools import pairwise

data = []

def issafe(report):
    pairs = pairwise(report)
    diffs = np.array([np.subtract(*i) for i in pairs])
    if not (np.all(diffs > 0) or np.all(diffs < 0)):
        return False
    elif np.any(np.abs(diffs) > 3):
        return False
    return True

with open('./input.txt') as file:
    for line in file.readlines():
        values = line.strip().split(' ')
        data.append([int(i) for i in values])

print(np.sum([issafe(report) for report in data]))