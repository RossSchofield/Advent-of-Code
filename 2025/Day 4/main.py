from scipy.ndimage import convolve
import numpy as np

with open('input.txt', 'r') as file:
    map_ = [[1 if i == '@' else 0 for i in line.strip()] for line in file]

kernel = [[1,1,1], [1,0,1], [1,1,1]]

adj = convolve(map_, kernel, mode='constant', cval=0)
print(np.logical_and(adj < 4, map_).sum())
