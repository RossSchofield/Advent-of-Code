# with open('input.txt', 'r') as file:
#     fresh = set()
#     while (line := file.readline().strip().split('-')) != ['']:
#         fresh |= set(range(int(line[0]), int(line[1]) + 1))
#     available = [int(i.strip()) for i in file]
#
# print(sum([i in fresh for i in available]))

with open('input.txt', 'r') as file:
    fresh = []
    while (line := file.readline().strip().split('-')) != ['']:
        fresh.append(range(int(line[0]), int(line[1]) + 1))
    available = [int(i.strip()) for i in file]

print(sum([any(i in range_ for range_ in fresh) for i in available]))