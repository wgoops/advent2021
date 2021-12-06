import copy
import pytest
# the input was manually broken into two files: nums.txt and boards.txt

# nums.txt contains the numbers drawn in the bingo raffle. We want to make this a list of integers. 
with open("nums.txt") as f: 
    raw_nums = f.read().split(",")
nums = [int(num) for num in raw_nums]

# no further processing of nums.txt is needed. 

# boards.txt contains the bingo boards. 
# to make life simple, we don't want to check every bingo board every time. 
# what we will do is make a list, "boards". 
# in this list, we will store the boards. 
# we will then store the rows of each board. 
# here's the neat part: we explicitly store the columns, too. 
# so, say we have the following bingo board: 

#   10 20 33 
#   40 53 60
#   70 80 90 

# an entry in "boards" would be: 
#  [[10, 20, 33] 
#   [40, 53, 60]
#   [70, 80, 90] 
#   [10, 40, 70]
#   [20, 53, 80]
#   [33, 60, 90]

# this will keep the state of whether or not a board has won. 

# we can now search through boards for numbers. 
# I am going to be performing a linear search because I am a simple man. 

# the clever approach is to do the search via a dict. 
# the dict uses the number as the key, and the location in boards as its value. 
# then, from there, we can search much more efficiently. 
# since my approach doesn't have to scale, idc. 
# anyways: 
 
raw_boards = []
with open("boards.txt") as f: 
    raw_boards = f.read().splitlines()

boards = []
sheet = []

for row in raw_boards: 
    if row == "": 
        boards.append(copy.deepcopy(sheet))
        sheet = []
    else:
        int_row = []
        for col in row.split(): 
            int_row.append(int(col))
        sheet.append(copy.deepcopy(int_row))

winning_rows = boards
winning_columns_for_board = [[None, None, None, None, None] for i in range(len(boards[0]))]
winning_columns = [copy.deepcopy(winning_columns_for_board) for board in boards]

for b in range(len(boards)):
    for r in range(len(boards[b])):
        for c in range(len(boards[b][r])):
            winning_columns[b][c][r] = boards[b][r][c]

# time to search.

def boardSearch(nums, boards, winning_rows, winning_columns):
    for num in nums: 
        for b in range(len(boards)): 
            for r in range(len(boards[b])):

                for c in range(len(boards[b][r])):
                    if winning_rows[b][r][c] == num: 
                        winning_rows[b][r][c] = None
                        boards[b][r][c] = None

                    if winning_columns[b][r][c] == num: 
                        winning_columns[b][r][c] = None

                if winning_rows[b][r] == [None, None, None, None, None]:
                    winning_board = boards[b]
                    breakpoint()
                    return b, num, winning_board
                elif winning_columns[b][r] == [None, None, None, None, None]:
                    winning_board = boards[b]
                    breakpoint()
                    return b, num, winning_board


b, num, winning_board = boardSearch(nums, boards, winning_rows, winning_columns)

board_sum = 0
for row in winning_board: 
    for entry in row: 
        if entry != None: 
            board_sum += entry

result = board_sum * num
breakpoint()