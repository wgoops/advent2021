with open("data.txt") as f: 
    data = f.read().splitlines()
    
octos = [[] for line in data]
flash_count = 0
for i in range(len(data)): 
    for char in data[i]: 
        octos[i].append(int(char))

def neighbors(octo):
    row = octo[0]
    col = octo[1]
    
    coords = [(-1, -1),
              (-1, 0),
              (-1, 1), 
              (0, -1), 
              (0, 1), 
              (1, -1), 
              (1, 0), 
              (1, 1)]
    
    #check bottom 
    if row == len(octos) - 1: 
        for coord in [(1, -1), (1, 0), (1, 1)]:
            if coord in coords: coords.remove(coord) 
        
    # check top
    if row == 0:
        for coord in [(-1, -1), (-1, 0), (-1, 1)]:
            if coord in coords: coords.remove(coord) 
    
    #check right
    if col == len(octos[row]) - 1: 
        for coord in [(-1, 1), (0, 1), (1, 1)]:
            if coord in coords: coords.remove(coord)

    #check left
    if col == 0:
        for coord in [(-1, -1), (0, -1), (1, -1)]:
            if coord in coords: coords.remove(coord) 

    return [(row+coord[0], col + coord[1]) for coord in coords]

flash_count = 0

def flasher(octo):
    i = octo[0]
    j = octo[1]
    if octos[i][j] > 9: 
        global flash_count
        flash_count = flash_count + 1
        #breakpoint()
    
        flashed[i][j] = True

        for coord in neighbors(octo): 
            row = coord[0]
            col = coord[1]
            octos[row][col] = octos[row][col] + 1

            if not flashed[row][col]:
                flasher(coord)


step = 1

zeros = [[0 for num in octos[0]] for line in octos]


while octos != zeros: 
        
    flashed = [[False for num in octos[0]] for line in octos]

    for i in range(len(octos)):
        for j in range(len(octos[i])):
            octos[i][j] = octos[i][j] + 1
    
    for i in range(len(octos)):
        for j in range(len(octos[i])):
            if not flashed[i][j]:
                flasher((i, j))
    
    for i in range(len(octos)): 
        for j in range(len(octos[i])): 
            if octos[i][j] > 9: 
                octos[i][j] = 0
    
    
    step += 1
    print(step)
    
final_step = step - 1
print(f"final step: {final_step}")
for row in octos: 
    print(row)