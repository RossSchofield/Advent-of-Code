stones = []

with open('input.txt') as file:
    for stone in file.readline().strip().split(' '):
        stones.append(int(stone))

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif (size := len(str(stone))) % 2 == 0:
            new_stones.append(int(str(stone)[:size//2]))
            new_stones.append(int(str(stone)[size//2:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones

for i in range(75):
    stones = blink(stones)
print(len(stones))