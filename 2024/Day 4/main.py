import numpy as np


wordsearch = []
valid_words = np.array((('X', 'M', 'A', 'S'), ('S', 'A', 'M', 'X')))
found = 0

with open('input.txt') as file:
    for line in file:
        wordsearch.append([char for char in line.strip()])

diagonals = []
wordsearch = np.array(wordsearch)
mirrored = np.flip(wordsearch, axis=1)
verticals = np.rot90(wordsearch)
rows, columns = wordsearch.shape

for i in range(-rows, columns):
    diagonals.append(wordsearch.diagonal(i))
    diagonals.append(mirrored.diagonal(i))

for line in wordsearch:
    for i in range(rows - 3):
        slice = line[i:i+4]
        if (slice == valid_words).all(axis=(1)).any():
            found += 1
for column in verticals:
    for i in range(columns - 3):
        slice = column[i:i+4]
        if (slice == valid_words).all(axis=(1)).any():
            found += 1
for diagonal in diagonals:
    if len(diagonal) < 4:
        continue
    for i in range(len(diagonal) - 3):
        slice = diagonal[i:i+4]
        if np.array_equal(slice, valid_words[0]) or np.array_equal(slice, valid_words[1]):
            found += 1
print(found)