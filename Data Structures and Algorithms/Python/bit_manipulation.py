def getBit(num, bit_index):
    """Function to get the bit at a particular position
    
    Returns 0 or power of 2 to the bit_index"""
    return num & (1 << bit_index)

def set_bit(num, bit_index):
    """Function to set the bit at a particular position
    
    The mask retains all the original bits while enforcing a binary one at the specified index. 
    Had that bit already been set, its value wouldn't have changed.
    """
    return num | (1 << bit_index)

if __name__ == '__main__':
    print(getBit(0b10000000, 2))
    print(getBit(0b10100000, 5))
    print(set_bit(0b11, 4))
    print(bin(19))