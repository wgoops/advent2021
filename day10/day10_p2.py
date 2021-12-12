import copy 

with open("data.txt") as f: 
    data = f.read().splitlines()

#alright, so uh 

#lets remove brackets over and over again 

#cleaned = []
badEntries = ['[}', '[)', '[>', '{]', '{)', '{>', '(]', '(}', '(>', '<]', '<}', '<)']

goodEntries = {"[": "]",
               "{": "}", 
               "<": ">",
               "(": ")"}

corruptScore = 0
corruptScoreDict = {")": 3, 
             "]": 57, 
             "}": 1197,
             ">": 25137}

incompleteScoreDict =   {")": 1, 
                        "]": 2, 
                        "}": 3,
                        ">": 4}
incompleteScoreList = []
for i in range(len(data)):
    oldLength = -1000
    newLength = 1
    newLine = data[i]
    
    willComplete = ""
    while oldLength != newLength:
        oldLength = len(newLine)
        newLine = newLine.replace("{}", "")
        newLine = newLine.replace("[]", "")
        newLine = newLine.replace("()", "")
        newLine = newLine.replace("<>", "")
        newLength = len(newLine)
    #cleaned.append(copy.deepcopy(newLine))
    oldCorruptScore = corruptScore
    for entry in badEntries: 
        if entry in newLine: 
            corruptScore += corruptScoreDict[entry[1]]
    if oldCorruptScore == corruptScore:
        incompleteScore = 0
        for entry in newLine[::-1]: 
            willComplete += goodEntries[entry]
        for entry in willComplete: 
            incompleteScore *= 5
            incompleteScore += incompleteScoreDict[entry]
        incompleteScoreList.append(copy.deepcopy(incompleteScore))         

print(sorted(incompleteScoreList)[round(len(incompleteScoreList)/2)])
breakpoint()