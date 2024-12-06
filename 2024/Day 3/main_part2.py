import re

with open('input.txt') as file:
    memory = file.read()

expression = "mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))"
valid = re.findall(expression, memory)

total = 0
do = True
for instruction in valid:
    if do and instruction[0] != '':
        total += int(instruction[0]) * int(instruction[1])
    else:
        do = True if (instruction[2] or instruction[3]) == 'do()' else False

print(total)