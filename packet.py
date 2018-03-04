def packet(crc,lenght,data,flag):

    packet=crc
    packet=packet << 8
    packet=packet | lenght &((1<<8)-1)
    packet=packet << 18
    packet=packet | data & ((1<<18)-1)
    packet=packet << 1
    packet=packet | flag & ((1<<1)-1)
    return packet

if __name__=="__main__":
    packet(7,12,147,0)
    
