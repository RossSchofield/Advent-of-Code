from math import floor

with open('input.txt', 'r') as file:
    rotations = [int(line.strip()[1:]) * (-1 if line[0] == 'L' else 1) for line in file]

pos = 50
count = 0
for rotation in rotations:
    next_pos = pos + rotation
    count += abs(floor(pos / 100) - floor(next_pos / 100))
    pos = next_pos

print(count)