import statistics

with open("data.txt") as f: 
    data = f.read()

nums = [int(num) for num in data.split(",")]
nums = sorted(nums)

position = statistics.mode(nums) 

diff = 0
best_diff = 0
for num in nums: 
    if num != position: 
        best_diff += abs(position - num)

best_position = statistics.mode(nums)
possible_values = sorted([statistics.median(nums), statistics.mode(nums)])
for position in range(possible_values[0], round(possible_values[1]+ 1)):
    diff = 0
    for num in nums: 
        # there's a smarter way of doing this, but I don't care
        if num != position: 
            diff += abs(position - num)
    if diff < best_diff: 
        best_diff = diff
        best_position = position
print(nums)
print(f"modes: {statistics.multimode(nums)}")
print(f"median: {statistics.median(nums)}")
print(f"position: {best_position} | difference: {best_diff}")