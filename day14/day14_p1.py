with open("data.txt") as f: 
    data = f.read().splitlines()

chain = data[0]
raw_mappings = map(lambda char: char.split(" -> "), data[2::])
mappings = {}

for item in raw_mappings:
    pair = item[0]
    toInsert = item[1] 
    mappings[pair] = toInsert

def stepper(chain) -> str:
    result = ""
    for i in range(len(chain)-1): 
        char = chain[i]
        pair = chain[i] + chain[i+1]
        new_pair = char + mappings[pair]
        result += new_pair
    result += chain[-1]
    return result

step = 1
total_steps = 10

while step <= total_steps:
    chain = stepper(chain)
    print(len(chain))
    step += 1

item_count = {}
for item in chain: 
    if item not in item_count: 
        item_count[item] = 1
    else: 
        item_count[item] += 1

sorted_vals = sorted(item_count.items(), key=lambda x: x[1])

min_letter, max_letter = sorted_vals[0][0], sorted_vals[-1][0]
print(f"min: {item_count[min_letter]}")
print(f"max: {item_count[max_letter]}")
print(f"difference: {item_count[max_letter] - item_count[min_letter]}")
