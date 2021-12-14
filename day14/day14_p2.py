#### open file ####
with open("data.txt") as f: 
    data = f.read().splitlines()

#### obtain chain ####
chain = data[0]

#### parse raw mapping string into two separate letters, paired ####
raw_mappings = map(lambda char: char.split(" -> "), data[2::])

#### create hashmap of how pairs are mapped to insertion letters ####
mappings = {}

for item in raw_mappings:
    pair = item[0]
    toInsert = item[1] 
    mappings[pair] = toInsert

#### function definition for stepper ####

def stepper(pair_count, letter_count):

    #### initialize the result pair count ####
    result_count = {}
    for pair in mappings.keys():
        result_count[pair] = 0

        # while the pairs change on each step, letter count doesn't. 
        #   therefore existing letter_count hashmap is fine

    #### generate new pair count and track the newly-added letters ####
    for pair in mappings.keys(): 
        if pair_count[pair] > 0: 
            letter = mappings[pair] # this is the letter to insert

            # there's two newly-generated pairs for each insertion. 
            #   example below: 
            #   starting chain is NCN. Mappings are NC -> H and CN -> B
            #   NC -> H creates NHC. This is NH and HC. Total H's increases by 1. 
            #   CN -> B creates CBN. This is CB and BN. Total B's increases by 1. 
            #   Total chain is NHCBN. Pairs are NH, HC, CB, BN. 
            #   
            result_count[pair[0] + letter] += pair_count[pair] 
            result_count[letter + pair[1]] += pair_count[pair]
            if mappings[pair] in letter_count: 
                letter_count[letter] += pair_count[pair]

            # if the letter isn't found in letter_count, we initialize it here. 
            else: 
                letter_count[letter] = 1

    return result_count, letter_count

#### initialize pair count ####
pair_count = {}
for pair in mappings.keys():
    pair_count[pair] = 0

for i in range(len(chain)-1):
    pair_count[chain[i] + chain[i+1]] += 1

#### initialize letter count ####
letter_count = {}
for char in chain: 
    if char not in letter_count: 
        letter_count[char] = 1
    else: 
        letter_count[char] += 1

#### initialize steps ####
step = 1
total_steps = 40

#### run through steps ####
while step <= total_steps:
    pair_count, letter_count = stepper(pair_count, letter_count)
    step += 1

#### sort values ####
sorted_vals = sorted(letter_count.items(), key=lambda x: x[1])

#### obtain min/max letter ####
min_letter, max_letter = sorted_vals[0][0], sorted_vals[-1][0]

#### print result ####
print(f"min: {letter_count[min_letter]}")
print(f"max: {letter_count[max_letter]}")
print(f"difference: {letter_count[max_letter] - letter_count[min_letter]}")