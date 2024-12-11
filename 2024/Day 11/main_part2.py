from functools import cache

stones = []

with open('input.txt') as file:
    for stone in file.readline().strip().split(' '):
        stones.append(int(stone))

@cache
def blink(stone, times):
    if times == 0:
        return 1

    if stone == 0:
        return blink(1, times - 1)
    elif (size := len(str(stone))) % 2 == 0:
        return blink(int(str(stone)[:size//2]), times - 1) + blink(int(str(stone)[size//2:]), times - 1)
    else:
        return blink(stone * 2024, times - 1)

print(sum([blink(stone, 75) for stone in stones]))

