import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")
with open("data.txt") as f:
    data = f.read().splitlines()

data_dict = {}
x, y = 0, 0
for item in data:
    split_item = item.split(" ")
    direction = split_item[0]
    magnitude = int(split_item[1])

    if direction == "forward":
        x += magnitude

    if direction == "up":
        y -= magnitude

    if direction == "down":
        y += magnitude

logging.info(f"x: {x}")
logging.info(f"y: {y}")
logging.info(f"x*y: {x*y}")
