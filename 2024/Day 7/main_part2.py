test_values = []
values = []

with open('input.txt') as file:
    for line in file:
        test_value, vals = line.strip().split(':')
        test_values.append(int(test_value))
        values.append([int(i) for i in vals[1:].split(' ')])

def concat(num1, num2):
    return int(str(num1) + str(num2))

def reduce(test_value, vals):
    if len(vals) == 1:
        return vals
    else:
        res = []
        for i in reduce(test_value, vals[:-1]):
            if i * vals[-1] <= test_value:
                res.append(i * vals[-1])
            if i + vals[-1] <= test_value:
                res.append(i + vals[-1])
            if concat(i, vals[-1]) <= test_value:
                res.append(concat(i, vals[-1]))
        return res

print(sum(test_value for test_value, vals in zip(test_values, values)
      if test_value in reduce(test_value, vals)))