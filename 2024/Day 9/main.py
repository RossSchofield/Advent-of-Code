with open('input.txt') as file:
    data = [-1 if id_ % 2 == 1 else id_//2 for id_, j in enumerate(file.readline()) for i in range(int(j))]

checksum = 0
right = len(data) - 1
for index, i in enumerate(data):
    if index > right:
        break
    if i == -1:
        while data[right] == -1:
            right -= 1
        if right > index:
            checksum += data[right] * index
            right -= 1
    else:
        checksum += i * index

print(checksum)
