# open file to get data
with open("data.txt") as f:
    data = f.read().splitlines()

data_indexes = range(len(data))
# convert data to list of integers
for i in data_indexes:
    data[i] = int(data[i])

count = 0
# compare previous item with current
for j in data_indexes[1::]:
    current = data[j]
    previous = data[j - 1]
    if current > previous:
        count += 1

print(count)
