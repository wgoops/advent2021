with open("data.txt") as f: 
    data = f.read().splitlines()

grid = [[int(node) for node in row] for row in data]

### dijkstra needs a couple of things. 

### first is weight of 0,0 to the end 

start = (0,0) # y,x

shortest_dict = {}
neighbors = {}
touched = {}
for y in range(len(grid)): 
    for x in range(len(grid[y])):
        shortest_dict[(y, x)] = {"cost": 999999999999999999999, 
                                 "previous_node": None, 
                                 "visited": False} 
        neighbors[(y, x)] = []
        touched[(y,x)] = False
        if y < len(grid) - 1: 
            neighbors[(y, x)].append((y+1, x))
        if y > 0: 
            neighbors[(y, x)].append((y-1, x))
        if x < len(grid[0]) - 1: 
            neighbors[(y, x)].append((y, x+1))
        if x > 0: 
            neighbors[(y, x)].append((y, x-1))

next = start
shortest_dict[start]["cost"] = 0

while next != None: 
    node = next
    ##### node edge calc #####
    
    for nbor in neighbors[node]:         
        if not shortest_dict[nbor]["visited"]: 
            touched[nbor] = True 

            edge_cost = grid[nbor[0]][nbor[1]]
            path_cost = shortest_dict[node]["cost"] + edge_cost
            if shortest_dict[nbor]["cost"] > path_cost:
                shortest_dict[nbor]["cost"] = path_cost
                shortest_dict[nbor]["previous_node"] = node
                
    shortest_dict[node]["visited"] = True
    smallest = {"previous_node": None, 
                "cost": 99999999999999999999999 }
    
    smallest_item = None
    
    for item in touched.keys(): 
        if shortest_dict[item]["cost"] < smallest["cost"] and not shortest_dict[item]["visited"]:
            smallest = shortest_dict[item]
            smallest_item = item
    
    next = smallest_item

path_sum = 0
goal_node = (len(grid)-1, len(grid[0])-1)
print(shortest_dict[goal_node]["cost"])




