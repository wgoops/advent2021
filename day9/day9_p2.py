import copy

with open("data.txt") as f: 
    data = f.read().splitlines()

height_grid = [[] for row in data]

for i in range(len(data)): 
    for num in data[i]: 
        height_grid[i].append(int(num))

# extremely awful memory-heavy approach to come up with adjacency list, 
#   since those are nicer to work with and I'm lazy 
# I am well-aware that it's not necessary
# but
# I am very suspicious that p2 will be something shitty 
# 
adjacency_list = {}
for i in range(len(height_grid)):
    row = height_grid[i]
    top_wall, bottom_wall, = False, False
    if i == 0: 
        top_wall = True
    if i == len(height_grid) - 1: 
        bottom_wall = True
    for j in range(len(row)):
        left_wall, right_wall = False, False
        if j == 0: 
            left_wall = True
        if j >= len(row) - 1:
            right_wall = True 
        
        adjacency_list[(i,j)] = []
        #print((i,j), left_wall, right_wall, top_wall, bottom_wall)
        if not right_wall:
            adjacency_list[(i,j)].append((i,j+1))
        if not left_wall: 
            adjacency_list[(i,j)].append((i,j-1))
        if not top_wall: 
            adjacency_list[(i,j)].append((i-1,j))
        if not bottom_wall: 
            adjacency_list[(i,j)].append((i+1,j))

risk_level = 0
# sorry 
checked_graph = [[False for i in range(len(height_grid[0]))] for j in range(len(height_grid))]

# DFS TIME DFS TIME DFS TIME DFS TIME DFS TIME DFS TIME 
node_sums = copy.deepcopy(checked_graph)


def dfs(coord, basin_size):
    i, j = coord
    adjacent_coords = adjacency_list[coord]
    basin_size += 1
    if height_grid[i][j] != 9: 
        for adj_coord in adjacent_coords: 
            k, l = adj_coord
            if height_grid[k][l] != 9 and not checked_graph[k][l]:
                checked_graph[k][l] = True
                basin_size = dfs(adj_coord, basin_size)
                node_sums[k][l] = basin_size

    return basin_size

basins = []
for coord in adjacency_list.keys():
    
    basins.append(dfs(coord,-1))

basins = sorted(basins)

for row in node_sums: 
    print(row)

print(basins[-3::])
result = 1
for n in basins[-3::]:
    result *= n
print(result)