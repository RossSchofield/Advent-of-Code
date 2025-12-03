import math
with open('input.txt', 'r') as file:
    ranges = [[int(j) for j in i.split('-')] for i in file.readline().strip().split(',')]

tot = 0
for id_range in ranges:
    for i in range(id_range[0], id_range[1]+1):
        n_digits = math.floor(math.log10(i))
        for j in range(1, n_digits//2 + 1):
            if n_digits % j == 0:
                if len(set(str(i)[j*k:j*(k+1)] for k in range(n_digits//j))) == 1:
                    tot += i
                    break

print(tot)
