import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
with open("data.txt") as f: 
    data = f.read().splitlines()


def oxyMatch(data, digit):

    total_digit_list = [0 for i in range(len(data[0]))]

    for item in data: 
        for i in range(len(data[0])): 
            total_digit_list[i] += int(item[i])

    if total_digit_list[digit]/len(data) >= .5: 
        oxy_match = "1"
    else: 
        oxy_match = "0"

    oxy_list = []
    for item in data: 
        if item[digit] == oxy_match:
            oxy_list.append(item)
        
    return oxy_list

def co2Match(data, digit):

    total_digit_list = [0 for i in range(len(data[0]))]

    for item in data: 
        for i in range(len(data[0])): 
            total_digit_list[i] += int(item[i])

    if total_digit_list[digit]/len(data) >= .5: 
        co2_match = "0"
    else: 
        co2_match = "1"

    co2_list = []
    for item in data: 
        if item[digit] == co2_match:
            co2_list.append(item)
        
    return co2_list

oxy_list = oxyMatch(data, 0)
co2_list = co2Match(data, 0)

i = 1
while len(oxy_list) > 1: 
    oxy_list = oxyMatch(oxy_list, i)
    i += 1

j = 1
while len(co2_list) > 1: 
    co2_list = co2Match(co2_list, j)
    j += 1

logging.info(f"oxy_list: {oxy_list}")
logging.info(f"co2_list: {co2_list}")

oxy_rating = int("0b" + oxy_list[0], 2)
co2_rating = int("0b" + co2_list[0], 2)
oxy_co2_multiplied = oxy_rating*co2_rating

logging.info(f"oxy_rating: {oxy_rating}")
logging.info(f"co2_rating: {co2_rating}")
logging.info(f"oxy_co2_multiplied: {oxy_co2_multiplied}")