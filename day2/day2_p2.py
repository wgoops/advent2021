import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")
with open("data.txt") as f:
    data = f.read().splitlines()

data_dict = {}
x, y, aim = 0, 0, 0
for item in data:
    split_item = item.split(" ")
    direction = split_item[0]
    magnitude = int(split_item[1])

    if direction == "forward":
        x += magnitude
        y += aim * magnitude

    if direction == "up":
        aim -= magnitude

    if direction == "down":
        aim += magnitude
logging.info(f"x: {x}")
logging.info(f"y: {y}")
logging.info(f"aim: {aim}")
logging.info(f"x*y: {x*y}")
