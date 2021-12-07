import copy
from os import error 

with open("data.txt") as f: 
    data = f.read().splitlines()

pairs = []

for pair in data: 
    tmp = pair.split(" -> ")
    tmp = [tmp[0].split(","), tmp[1].split(",")]
    tmp = [(int(tmp[0][0]), int(tmp[0][1])),
           (int(tmp[1][0]), int(tmp[1][1]))]
    pairs.append(copy.deepcopy(tmp))

grid = [[0 for x in range(1000)] for y in range(1000)]

def fill_in(pairs, grid):
    for pair in pairs: 
        x1 = pair[0][0]
        y1 = pair[0][1]
        x2 = pair[1][0]
        y2 = pair[1][1]

        if x1 == x2: 
            # we fill in vertically
            if y2 > y1: 
                for y in range(y1, y2 + 1):
                    grid[y][x1] += 1
            else: 
                for y in range(y2, y1 + 1):
                    grid[y][x1] += 1
        elif y1 == y2: 
                # we fill in horizontally
            if x2 > x1: 
                for x in range(x1, x2 + 1):
                    grid[y1][x] += 1
            else: 
                for x in range(x2, x1 + 1):
                    grid[y1][x] += 1

        else: 
            # eat shit 
            print(f"Points {pair} are diagonal")
    return grid

grid = fill_in(pairs, grid)
danger_count = 0

for horizontals in grid: 
    for point in horizontals: 
        if point >= 2:
            danger_count += 1

print(f"danger_count: {danger_count}")