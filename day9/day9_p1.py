with open("data_test.txt") as f: 
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
local_min_list = {}
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
for coord in adjacency_list.keys():
    i = coord[0]
    j = coord[1]
    height = height_grid[i][j]
    point_is_local_min = True
    #print(f"coord:{coord}")
    for neighbor in adjacency_list[coord]:
        k = neighbor[0]
        l = neighbor[1]
        neighbor_height = height_grid[k][l]
        if neighbor_height <= height: 
            point_is_local_min = False 

    if point_is_local_min: 
        risk_level += 1 + height
        print("coord is local min")

        
        
breakpoint()