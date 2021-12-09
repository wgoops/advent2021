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

# so first, let's represent the correct signal mapping
#   0:      1:      2:      3:      4:
# aaaa    ....    aaaa    aaaa    ....
#b    c  .    c  .    c  .    c  b    c
#b    c  .    c  .    c  .    c  b    c
# ....    ....    dddd    dddd    dddd
#e    f  .    f  e    .  .    f  .    f
#e    f  .    f  e    .  .    f  .    f
# gggg    ....    gggg    gggg    ....

#  5:      6:      7:      8:      9:
# aaaa    aaaa    aaaa    aaaa    aaaa
#b    .  b    .  .    c  b    c  b    c
#b    .  b    .  .    c  b    c  b    c
# dddd    dddd    ....    dddd    dddd
#.    f  e    f  .    f  e    f  .    f
#.    f  e    f  .    f  e    f  .    f
# gggg    gggg    ....    gggg    gggg

def signal_subtractor(first,second): 
    result = first
    for letter in second: 
        result = result.replace(letter,"")
    return result

def signal_mapper(signals):

    signal_mapping = { 
        "a":"", 
        "b":"", 
        "c":"", 
        "d":"", 
        "e":"", 
        "f":"", 
        "g":""
    }
    
    signals = sorted(signals)
    for signal in signals: 
        if len(signal) == 2:
            one = signal
        if len(signal) == 3: 
            seven = signal
        if len(signal) == 4: 
            four = signal 
        if len(signal) == 7:
            eight = signal 
    
    # 1. get A mapping 
    
    a_map = signal_subtractor(seven, one)
    print(f"a_map: {a_map}")
    # 2. get G mapping by...
    #   ...identifying 9, then subtracting a_map from it 
     
    for signal in signals: 
        if len(signal) == 6:
            result = signal_subtractor(signal, four)
            if len(result) == 2:
                g_map = signal_subtractor(result, a_map)
    #            print(f"g_map: {g_map}")

    # 3. get D mapping by...
    #   ... identifying 3, then subtracting one, a_map and g_map from it 
    
    for signal in signals: 
        if len(signal) == 5: 
            result = signal_subtractor(signal, one + a_map + g_map)
            if len(result) == 1: 
                d_map = result
    #            print(f"d_map: {d_map}")

    # 4. get B mapping by... 
    #   ... subtracting one+d_map from four 
    
    b_map = signal_subtractor(four, (one + d_map))
    #print(f"b_map: {b_map}")

    # 5. get F mapping by... 
    #   ... subtracting a_map + d_map + g_map + b_map from a five-length signal...
    #   ... and seeing if only one letter is left 
    
    for signal in signals: 
        if len(signal) == 5: 
            result = signal_subtractor(signal, a_map + b_map + d_map + g_map)
            if len(result) == 1: 
                f_map = result
    #            print(f"f_map: {f_map}")
                
    # 6. get C map in similar way to B map 
    c_map = signal_subtractor(one,f_map)
    #print(f"c_map: {c_map}")

    # 7. finally, get E map in similar way to B map 
    e_map = signal_subtractor(eight, a_map + b_map + c_map + d_map + f_map + g_map)
    #print(f"e_map: {e_map}")

    signal_mapping[a_map] = "a"
    signal_mapping[d_map] = "d"
    signal_mapping[g_map] = "g"
    signal_mapping[b_map] = "b"
    signal_mapping[f_map] = "f"
    signal_mapping[c_map] = "c"
    signal_mapping[e_map] = "e"
    
    return signal_mapping

def output_fixer(mapping, scrambled_output_list):
    
    correct_signals = {
        "".join(sorted("cf")):"1",
        "".join(sorted("acf")):"7", 
        "".join(sorted("bcdf")):"4",
        "".join(sorted("acdeg")):"2",
        "".join(sorted("acdfg")):"3",
        "".join(sorted("abdfg")):"5",
        "".join(sorted("abdefg")):"6",
        "".join(sorted("abcdfg")):"9",
        "".join(sorted("abcefg")):"0",
        "".join(sorted("abcdefg")):"8"
    }
    
    unscrambled = []
    for scrambled_output in scrambled_output_list: 
        # i am a sinner 
        # map(lambda i : mapping[i], scrambled_output) will 
        #   convert the scrambled letters to the unscrambled
        # we want to sort these though, so that they can be looked up easily in our correct_signals dict 
        # join(sorted("dbfc") will output "bcdf", which is nice and easy to look up 
        unscrambled.append("".join(sorted(map(lambda i : mapping[i], scrambled_output))))
    
    nums = ""
    for num in unscrambled: 
        nums+=correct_signals[num]
    nums = int(nums)        
    
    return nums

fixed_outputs = []
for entry in data: 
    signals = entry[0]
    outputs = entry[1]

    mapping = signal_mapper(signals)
    fixed_outputs.append(output_fixer(mapping,outputs))

sum_of_outputs = 0
for num in fixed_outputs: 
    print(num)
    sum_of_outputs += num
    
print(f"sum of outputs: {sum_of_outputs}")
