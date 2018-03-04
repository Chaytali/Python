##WAP to accept the following from user CRC(3,7),lenght(7,12),data(16,142),flag(1,0),protocol type(4,4).
##(bits,value)


def packetization(crc,length,data,flag,prototype):
    p1=crc
    print("{:b}".format(p1))
    p1=p1<<7
    print("{:b}".format(p1))
    p1=p1|length&((1<<7)-1)
    print("{:b}".format(p1))
    p1=p1<<16
    p1=p1|data&((1<<16)-1)
    p1=p1<<1
    p1=p1|flag&((1<<1)-1)
    p1=p1<<4
    p1=p1|prototype&((1<<4)-1)
    return(p1)

def depacketization(packet):
    protype= packet & ((1<<4)-1)
    print("{:b}".format(protype))


if __name__=='__main__':
    x=packetization(7,12,142,0,4)
    print("the value is","{:b}".format(x))
    depacketization(x)
