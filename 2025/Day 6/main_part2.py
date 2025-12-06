from functools import reduce
from operator import add, mul

with open('input.txt', 'r') as file:
    raw = zip(*file.readlines())

ops = []
numbers = []
for i in raw:
    if i[-1] != ' ':
        op = mul if i[-1] == '*' else add
        nums = []
    if set(i) == {' '}:
        ops.append(op)
        numbers.append(nums)
        continue
    nums.append(int(''.join(i[:-1])))
ops.append(op)
numbers.append(nums)

print(sum(reduce(op, number) for op, number in zip(ops, numbers)))