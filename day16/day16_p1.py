def hex2bin(hex_val):
    return bin(int(hex_val, base=16))[2::]
 
 
def bin2int(bin_val):
    return int("0b" + bin_val, base=2)

    
def getHeaders(packet):
    version = bin2int(packet[0:3])
    type_id = bin2int(packet[3:6])

    return version, type_id



def packet_type(packetbits): 
    version, type_id = getHeaders(packetbits)
    print(type_id)
    if type_id == 4: #type is operator
        return literal_packet
    else:         
        if packetbits[6] == "1": 
            return operator_bitlength
        else: 
            return operator_subpackets

def literal_packet(packet):
    packetbits = packet.packetbits[6::]
    #### binary_parser ####
    
    #### group the packet into groups of five ####
    indexes = range(0, len(packetbits) - 1, 5)  # we can disregard the extra bits at the end 
    print(indexes)
    bin_list = []
    for i in range(len(indexes) - 1): 
        j_start = indexes[i]
        j_end = indexes[i+1]
        bin_list.append(packetbits[j_start:j_end])
        if packetbits[j_start] == 0: 
            break
    full_num = ""
    for item in bin_list: 
        full_num = full_num + item[1::]
    
    return bin2int(full_num)

def operator_bitlength(packet):
    packetbits = packet.packetbits[7::]
    total_len_in_bits = bin2int(packetbits[0:15])
    sub_packets = packetbits[15:(15 + total_len_in_bits)]

    return sub_packets

def operator_subpackets(packet): 
    packet = packet.packetbits[7::]

    return 0 

# from https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm


class Tree:
   def __init__(self):
      self.headval = None

class Packet:
    def __init__(self, packet):
        self.packetbits = packet
        self.version, self.type_id = getHeaders(self.packetbits)
        self.packfunc = packet_type(packet)
        self.nextPackets = self.packfunc(packet)


def main(): 
    packet = hex2bin("8A004A801A8002F478")

    tree1 = Tree()
    tree1.headval = Packet(packet)
    

main()


def test_hex2bin():
    assert hex2bin("1AB") == "110101011"
    
def test_bin2hex(): 
    assert bin2int("110101011") == 427

def test_getHeaders(): 
    packetbits = "110101011"
    assert getHeaders(packetbits) == (6, 5)

def test_literal_packet(): 
    packet = Packet("110100101111111000101000")   #this packet is from the example
    assert literal_packet(packet) == 2021 

def test_packet_type_literal():
    packet = Packet("110100101111111000101000")
    assert packet_type(packet.packetbits) == literal_packet

def test_operator_total_len_bits():
    packet = Packet("00111000000000000110111101000101001010010001001000000000")
    assert operator_bitlength(packet) == "110100010100101001000100100"