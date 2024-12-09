def display(files, free_space, size=42):
    a = ['.'] * size
    for file in files:
        for i in range(file[2], file[2] + file[1]):
            a[i] = str(file[0])
    for i in free_space:
        for j in range(i[1], i[1] + i[0]):
            a[j] = '.'

    print(''.join(a))

files = []
free_space = []
with open('input.txt') as file:
    pos = 0
    for id_, i in enumerate(file.readline()):
        if id_ % 2 == 0:
            files.append([id_//2, int(i), pos])
        elif int(i) > 0:
            free_space.append([int(i), pos])
        pos += int(i)

for file in reversed(files):
    for free in free_space:
        if free[1] > file[2]: # If free space is to right of data
            free_space.remove(free)
        elif free[0] >= file[1]:     # If file smaller than free block
            file[2] = free[1]        # Move file to start of free block
            if free[0] != file[1]:   # If free block not filled by data
                free[0] -= file[1]   # Shrink block size
                free[1] += file[1]   # and move start of block to the right
            else:
                free_space.remove(free)
            break

checksum = 0
for file in files:
    for i in range(file[2], file[2]+file[1]):
        checksum += file[0] * i
print(checksum)
