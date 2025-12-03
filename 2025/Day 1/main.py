with open('input.txt', 'r') as file:
    rotations = [int(line.strip()[1:]) * (-1 if line[0] == 'L' else 1) for line in file]

pos = 50
count = 0
for rotation in rotations:
    pos = (pos + rotation) % 100
    if pos == 0:
        count += 1

print(count)