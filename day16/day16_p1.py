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
    
    bin_list = [num[i:i+5] for i in range(len(packet) / 5)
    for num in bin_list: 
def test_hex2bin():
    assert hex2bin("1AB") == "110101011"
    

def test_bin2hex(): 
    assert bin2int("110101011") == 427


def test_getHeaders(): 
    packet = "1AB"
    assert getHeaders(packet) == (6, 5)

