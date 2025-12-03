with open('input.txt', 'r') as file:
    joltages = [[int(i) for i in line.strip()] for line in file]

total = 0
for row in joltages:
    for i in range(len(row)-12):
        for i in range(len(row)-1):
            if row[i+1] > row[i]:
                row.pop(i)
                break
        else:
            row.pop(-1)
    total += int(''.join(map(str, row)))

print(total)