import copy 

with open("data.txt") as f: 
    data = f.read().splitlines()

#alright, so uh 

#lets remove brackets over and over again 

#cleaned = []
badEntries = ['[}', '[)', '[>', '{]', '{)', '{>', '(]', '(}', '(>', '<]', '<}', '<)']
score = 0
scoreDict = {")": 3, 
             "]": 57, 
             "}": 1197,
             ">": 25137}

for i in range(len(data)):
    oldLength = -1000
    newLength = 1
    newLine = data[i]
    while oldLength != newLength:
        oldLength = len(newLine)
        newLine = newLine.replace("{}", "")
        newLine = newLine.replace("[]", "")
        newLine = newLine.replace("()", "")
        newLine = newLine.replace("<>", "")
        newLength = len(newLine)
    #cleaned.append(copy.deepcopy(newLine))
    for entry in badEntries: 
        if entry in newLine: 
            score += scoreDict[entry[1]]


print(score)
breakpoint()