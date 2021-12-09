with open("data.txt") as f: 
    data_raw = f.read().splitlines()
    
####get data in a sane format
#remove newlines
data_raw = [entry.split(" | ") for entry in data_raw]
#get signals and display outputs in pairs
data = []
for entry in data_raw:
    signals = entry[0].split()
    output = entry[1].split()
    data.append((signals, output))
    print(entry)

#now that our data's alright, we can see if the outputs contain one of the following: 
#    num  segments used
#     1 | 2 
#     4 | 4
#     7 | 3
#     8 | 7 

#we'll be lazy and just store these in a hashtable or something. 
# I got a feeling part 2 will be much more annoying 

nums = {2:1,
        4:4,
        3:7,
        7:8}

unique_count = 0 
for entry in data: 
    signals = entry[0]
    outputs = entry[1]
    for output in outputs: 
        if len(output) in nums: 
            unique_count += 1

print(unique_count)