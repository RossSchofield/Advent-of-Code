import numpy as np
import time

map_ = []
position = []
direction = np.array([-1j, -1])

with open('input.txt') as file:
    for y, line in enumerate(file):
        obstructions = []
        for x, char in enumerate(line.strip()):
            if char == '.':
                obstructions.append(0)
            elif char == '^':
                obstructions.append(0)
                position = np.array([x, y])
            else:
                obstructions.append(1)
        map_.append(obstructions)

map_=np.array(map_)
size = np.shape(map_)
visited = np.zeros(size)

while True:
    next_pos = position + np.real(direction).astype(int)
    if next_pos[0] < 0 or next_pos[0] >= size[0] or next_pos[1] < 0 or next_pos[1] >= size[1]:
        left_area = True
        break
    if map_[next_pos[1]][next_pos[0]] == 1:
        direction *= 1j
    else:
        visited[position[1]][position[0]] = 1
        position = next_pos


visited[position[1]][position[0]] = 1
print(np.sum(visited))
print(visited)