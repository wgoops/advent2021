def hex2bin(hex_val):
    return bin(int(hex_val, base=16))[2::]
 
 
def bin2int(bin_val):
    return int("0b" + bin_val, base=2)

    
def getHeaders(packet):
    bin_packet = hex2bin(packet)
    version = bin2int(bin_packet[0:3])
    type_id = bin2int(bin_packet[3:6])

    return version, type_id

def literal_packet(packet):
    packet = packet[6::]
    #### binary_parser ####
    
    #### group the packet into groups of five ####
    indexes = range(0, len(packet) - 1, 5)  # we can disregard the extra bits at the end 
    print(indexes)
    bin_list = []
    for i in range(len(indexes) - 1): 
        j_start = indexes[i]
        j_end = indexes[i+1]
        bin_list.append(packet[j_start:j_end])
        if packet[j_start] == 0: 
            break
    full_num = ""
    for item in bin_list: 
        full_num = full_num + item[1::]
    
    return bin2int(full_num)


def test_hex2bin():
    assert hex2bin("1AB") == "110101011"
    

def test_bin2hex(): 
    assert bin2int("110101011") == 427


def test_getHeaders(): 
    packet = "1AB"
    assert getHeaders(packet) == (6, 5)

def test_literal_packet(): 
    packet = "110100101111111000101000"   #this packet is from the example
    assert literal_packet(packet) == 2021 