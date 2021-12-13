with open("data.txt")as f: 
    raw_data = f.read().splitlines()


instructions_started = False
raw_dots = []
raw_instructions = []

for row in raw_data: 
    if row != "": 
        if instructions_started:
            raw_instructions.append(row)
        else: 
            raw_dots.append(row)
    
    else: 
        instructions_started = True 

raw_dots = [coord.split(",") for coord in raw_dots]
dots = map(lambda x: (int(x[0]), int(x[1])), raw_dots)
    
instructions = []
for instruction in raw_instructions:
    if "y=" in instruction: 
        instructions.append(("y", int(instruction[instruction.index('=')+1::])))
    elif "x=" in instruction:
        instructions.append(("x", int(instruction[instruction.index('=')+1::])))


def array_init(coords_map): 
    x_max = 1 
    y_max = 1
    coords = []
    for coord in coords_map: 
        x = coord[0]
        y = coord[1]
        print(coord)
        if x_max < x:
            x_max = x
        if y_max < y: 
            y_max = y
        coords.append(coord)
            
        
    grid = [["." for x in range(x_max + 1)] for y in range(y_max + 1)]
    coords = list(coords)
    for coord in coords: 
        x = coord[0]
        y = coord[1]
        grid[y][x] = "#"
    return grid

def horizontal_mirror(array):
    return [row[::-1] for row in array]

def vertical_mirror(array):
    return array[::-1]
#def up_folder(fold_location):

paper = array_init(dots)
tmp = []
new_grid = []
instruction = instructions[0]

#    print("###########")
#    for row in paper: 
#        print(row)
fold = instruction[0]
location = instruction[1]
if fold == "y": 
    new_grid = vertical_mirror(paper[location+1::])
    paper = paper[0:location]

if fold == "x": 
    new_grid = horizontal_mirror([row[location+1::] for row in paper])
    paper = [row[0:location] for row in paper]

for i in range(len(paper)):
    for j in range(len(paper[i])): 
        try: 
            if new_grid[i][j] == '#':
                paper[i][j] = new_grid[i][j]
        except Exception: 
            breakpoint()
            
print("######")
dot_count = 0
for row in paper: 
    #print(row)  
    for item in row: 
        if item == "#":
            dot_count += 1
print(f"dot_count: {dot_count}")

