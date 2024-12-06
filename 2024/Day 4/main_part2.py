import numpy as np

wordsearch = []
valid = np.array((('M', 'A', 'S'), ('S', 'A', 'M')))
found = 0

with open('input.txt') as file:
    for line in file:
        wordsearch.append([char for char in line.strip()])

wordsearch = np.array(wordsearch)
rows, columns = wordsearch.shape

for i in range(columns - 2):
    for j in range(rows - 2):
        block = wordsearch[i:i+3,j:j+3]
        if (block.diagonal(0) == valid).all(axis=(1)).any() and \
            (np.fliplr(block).diagonal(0) == valid).all(axis=(1)).any():

            found += 1

print(found)