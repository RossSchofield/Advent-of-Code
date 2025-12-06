from functools import reduce
from operator import add, mul

with open('input.txt', 'r') as file:
    data = file.readlines()
print(data)
numbers = [[int(i) for i in line.strip().split(' ') if i] for line in data[:-1]]
ops = [mul if i == '*' else add for i in data[-1].strip().split(' ') if i]

print(sum(reduce(op, number) for op, *number in zip(ops, *numbers)))
print(list(zip(ops, *numbers)))