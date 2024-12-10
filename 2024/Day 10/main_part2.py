import numpy as np

directions = np.array([(1,0), (0,1), (-1,0), (0,-1)])

with open('input.txt') as file:
    map_ = np.array([[int(i) for i in line.strip()] for line in file.readlines()])

width, height = map_.shape


def check_reachable(pos):
    if map_[pos[1]][pos[0]] == 9:
        return [tuple(pos)]

    a = []
    for direction in directions:
        next_ = pos + direction
        if 0 <= next_[0] < height and 0 <= next_[1] < width and map_[next_[1]][next_[0]] - map_[pos[1]][pos[0]] == 1:
            for i in check_reachable(next_):
                a.append(i)
    return a


total = 0
for y, line in enumerate(map_):
    for x, char in enumerate(line):
        if char == 0:
            peaks = check_reachable([x, y])
            print(peaks)
            score = len(peaks)
            total += score

print(total)
