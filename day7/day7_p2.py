import statistics

with open("data.txt") as f: 
    data = f.read()

nums = [int(num) for num in data.split(",")]
nums = sorted(nums)

position = statistics.mode(nums) 

# Fuel Cost using Dynamic Programming
def fuel_cost_gen(n): # stolen from https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
     
    # Taking 1st two fibonacci numbers as 0 and 1
    f = [1,3]
    
    for i in range(2, n+1):
        this_step_cost = i + 1
        total_cost = this_step_cost + f[i-1]
        f.append(total_cost)
    return [0] + f

fuel_cost = fuel_cost_gen(max(nums))

best_diff = 0
for num in nums: 
    if num != position: 
        best_diff += fuel_cost[abs(position - num)]

best_position = statistics.mode(nums)
possible_values = sorted([statistics.median(nums), statistics.mode(nums)])
for position in range(min(nums), max(nums) + 1):
    diff = 0
    for num in nums: 
        # there's a smarter way of doing this, but I don't care
        if num != position: 
            diff += fuel_cost[abs(position - num)]
    if diff < best_diff: 
        best_diff = diff
        best_position = position

diff = 0

for num in nums: 
        # there's a smarter way of doing this, but I don't care
        if num != best_position: 
            diff += fuel_cost[abs(position - num)]
            print(f"pos: {position} | num: {num} | cost: {fuel_cost[abs(position - num)]} | diff: {diff}")
    
print(f"modes: {statistics.multimode(nums)}")
print(f"median: {statistics.median(nums)}")
print(f"position: {best_position} | difference: {best_diff}")