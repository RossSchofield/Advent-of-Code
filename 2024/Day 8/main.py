from itertools import combinations
import numpy as np

locations = {}
width = 0
height = 0

for i in range(48, 123):
    locations |= {chr(i): []}

with open('input.txt') as file:
    for y, line in enumerate(file):
        height = y
        for x, char in enumerate(line.strip()):
            if char != '.':
                locations[char].append((x, y))
    file.seek(0)
    width = len(file.readline().strip())

height += 1
antinode_map = np.zeros((height, width))

for frequency, antennas in locations.items():
    if len(antennas) > 1:
        for pair in combinations(antennas, 2):
            diff = np.subtract(pair[1], pair[0])
            antinodes = [
                np.subtract(pair[0], diff),
                np.add(pair[1], diff)
            ]
            for antinode in antinodes:
                x, y = antinode
                if 0 <= x < width and 0 <= y < height:
                    antinode_map[y][x] = 1

print(antinode_map)
print(int(sum(sum(antinode_map))))

