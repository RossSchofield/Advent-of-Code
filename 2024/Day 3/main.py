import re

with open('input.txt') as file:
    memory = file.read()

valid = re.findall(
    'mul\((\d+),(\d+)\)',
    memory
)


print(sum(
    int(pair[0]) * int(pair[1]) for pair in valid
))