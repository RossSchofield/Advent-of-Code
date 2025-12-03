with open('input.txt', 'r') as file:
    ranges = [[int(j) for j in i.split('-')] for i in file.readline().strip().split(',')]

tot = 0
for id_range in ranges:
    for i in range(id_range[0], id_range[1]+1):
        n_digits = len(str(i))
        if n_digits % 2 == 0:
            x, y = divmod(i, pow(10, n_digits//2))
            if (x := divmod(i, pow(10, n_digits//2)))[0] == x[1]:#if x == y:
                tot += i

print(tot)

tot2 = sum(i for id_range in ranges for i in range(id_range[0], id_range[1]+1)
           if (n_digits := len(str(i))) % 2 == 0 and (x := divmod(i, pow(10, n_digits//2)))[0] == x[1])
print(tot2)