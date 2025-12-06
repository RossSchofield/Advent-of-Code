from scipy.ndimage import convolve
import numpy as np

with open('input.txt', 'r') as file:
    map_ = [[1 if i == '@' else 0 for i in line.strip()] for line in file]

kernel = [[1,1,1], [1,0,1], [1,1,1]]

total = 0
while True:
    adj = convolve(map_, kernel, mode='constant', cval=0)
    valid = np.logical_and(adj < 4, map_).astype(int)
    if valid.sum() == 0:
        break
    total += valid.sum()
    map_ = np.logical_and(map_, 1 - valid).astype(int)

print(total)
