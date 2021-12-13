with open("data.txt") as f: 
    data = f.read().splitlines()

edges_raw = [edge.split("-") for edge in data]
edges = {}

for edge in edges_raw: 
    if not edge[0] in edges:
        edges[edge[0]] = []        
    if not edge[1] in edges: 
        edges[edge[1]] = []
    edges[edge[0]].append(edge[1])
    edges[edge[1]].append(edge[0])

paths = []
def dfs(path, small_cave_visited_twice, step = 0):
    #print(f"path:{path}")
    #print(f"node: {node}")
    # 1. look for neighbors
    node = path[-1] 
    neighbors = edges[node]
    
    if node == "end":
        #print(f"path ends: {path}")
        paths.append(path)
    else: 
        if "start" in neighbors: 
            neighbors.remove("start")
        
        for i in range(len(neighbors)): 
            neighbor = neighbors[i]
            
            if small_cave_visited_twice:          
                if neighbor.lower() == neighbor: 
                    if neighbor not in path: 
                        dfs(path + [neighbor], True, step + 1)
                else: 
                    dfs(path + [neighbor], True, step + 1)
        
            else: 
                if neighbor.lower() == neighbor:            # if it's a small cave...
                    occurances = path.count(neighbor)   # ... see how many times we've visited it. 
                    if occurances == 1: #idk why this can't be 2 but whatever man 
                        dfs(path + [neighbor], True, step + 1)  
                    else: 
                        dfs(path + [neighbor], False, step + 1)
                else: 
                    dfs(path + [neighbor], False, step + 1)
            
            
dfs(["start"], False)
print(len(paths))
