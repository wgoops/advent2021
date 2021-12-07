with open ("data.txt") as f: 
    data = f.read()

starting_fish = [int(x) for x in data.split(",")] 
fish_count = [0 for i in range(9)]

#we will store fish counts in a list, where the index is the days until the fish makes a new fish 

for fish in starting_fish: 
    fish_count[fish] += 1

def fish_breeder(fish_count):
    #first, shift all the fish over (we will deal with 0, 8, and 6 fish last)
    fish_to_breed = fish_count[0]
    for i_fish in range(1, 9):
        fish_count[i_fish - 1] = fish_count[i_fish]
    fish_count[8] = 0
    fish_count[8] += fish_to_breed
    fish_count[6] += fish_to_breed
    
    return fish_count 

days = 1
while days <= 80: 
    print(fish_count[::-1])
    print(f"days: {days}")
    fish_count = fish_breeder(fish_count)
    days += 1

total_fish = 0
for fish in fish_count: 
    total_fish += fish
print(total_fish)
