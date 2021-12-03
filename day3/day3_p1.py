import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

with open("data.txt") as f:
    data = f.read().splitlines()

# I guess we'll just work with the strings

# So, we will
# 1. sum the digits
# 2. see if the sum is >.50000000
# if yes, then the most common number for that digit is 1
# if no, then the most common number for that digit is 0
# 3. from there, we can make gamma and epsilon

digit_list = [0 for i in range(len(data[0]))]
for item in data:
    for i in range(len(data[0])):
        digit_list[i] += int(item[i])

gamma_rate = ""
episilon_rate = ""
# set gamma rate
for i in range(len(digit_list)):
    item_int = int(digit_list[i])
    gamma_average_value = round(item_int / len(data))

    # there's a more elegant way of doing this, but I'm lazy
    # there's also some edge cases I'm not handling; see above comment.
    if gamma_average_value == 0:
        episilon_average_value = 1
    else:
        episilon_average_value = 0

    gamma_rate += str(gamma_average_value)
    episilon_rate += str(episilon_average_value)

gamma_rate = "0b" + gamma_rate
episilon_rate = "0b" + episilon_rate

logging.info(f"gamma_rate (binary): {gamma_rate}")
logging.info(f"episilon_rate (binary): {episilon_rate}")

gamma_rate = int(gamma_rate, 2)
episilon_rate = int(episilon_rate, 2)
power_consumption = gamma_rate * episilon_rate
logging.info(f"gamma_rate: {gamma_rate}")
logging.info(f"episilon_rate: {episilon_rate}")
logging.info(f"power_comsumption: {power_consumption}")
