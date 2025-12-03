with open('input.txt', 'r') as file:
    joltages = [[int(i) for i in line.strip()] for line in file]

total = 0
for row in joltages:
    first = 0
    for i, j in enumerate(reversed(row)):
        if i != 0 and j >= row[first]:
            first = len(row) - i - 1
    second = 0
    for i in range(first + 1, len(row)):
        second = max(row[i], second)
    total += 10 * row[first] + second

print(total)