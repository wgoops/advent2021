# open file to get data
with open("data.txt") as f:
    data = f.read().splitlines()

data_indexes = range(len(data))
# convert data to list of integers
for i in data_indexes:
    data[i] = int(data[i])

count = 0
# compare previous item set with current
for j in data_indexes[3::]:

    # [1, 2, 3, 4]
    # current is [2 3 4]
    # previous is [1 2 3]

    window_4 = data[j]  # "end" of window
    window_3 = data[j - 1]
    window_2 = data[j - 2]
    window_1 = data[j - 3]  # "start" of window

    current_sum = window_4 + window_3 + window_2
    previous_sum = window_3 + window_2 + window_1
    if current_sum > previous_sum:
        count += 1

print(count)
