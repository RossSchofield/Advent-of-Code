import numpy as np
from scipy.signal import convolve2d

with open('input.txt') as file:
    map_ = np.array([[char for char in line.strip()] for line in file.readlines()])

height, width = map_.shape


def floodfill(map_, pos, visited=None):
    if visited is None:
        visited = {pos}

    region = {pos}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for direction in directions:
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if not (0 <= next_pos[0] < width and 0 <= next_pos[1] < height) \
                or next_pos in visited:
            continue
        visited.add(next_pos)
        if map_[next_pos[1], next_pos[0]]:
            region.add(next_pos)
            region = region.union(floodfill(map_, next_pos, visited))

    return region


def find_regions(map_):
    plants = np.unique(map_)
    regions = []
    for plant in plants:
        locations = map_ == plant
        for y in range(height):
            for x in range(width):
                if locations[y, x]:
                    region = floodfill(locations, (x,y))
                    regions.append(region)
                    for plot in region:
                        locations[plot[1], plot[0]] = False
    return regions


def find_perimeter(region):
    kernel = np.array([[0, 1, 0],
                       [1, 0, 1],
                       [0, 1, 0]])
    region_map = np.ones((height, width), dtype=bool)
    for plot in region:
        region_map[plot[1], plot[0]] = False
    edges = convolve2d(region_map, kernel, mode='same', boundary='fill', fillvalue=1)
    return sum(sum(edges * ~region_map))


regions = find_regions(map_)
print(sum(len(region) * find_perimeter(region) for region in regions))