with open('input.txt', 'r') as file:
    fresh = []
    while (line := file.readline().strip().split('-')) != ['']:
        start = int(line[0])
        end = int(line[1]) + 1
        curr = range(start, end)
        for i, range_ in enumerate(fresh):
            if start in range_ and end in range_:
                break
            elif start in range_:
                start = range_.stop
            elif end - 1 in range_:
                end = range_.start
            elif range_.start in curr and range_.stop - 1 in curr:
                fresh[i] = range(0,0)
        else:
            fresh.append(range(start, end))
    available = [int(i.strip()) for i in file]

print(sum(len(range_) for range_ in fresh))

