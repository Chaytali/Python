def encrpt():
    a,b,c,d=input("Enter the values crc,length,data,flag")
#    print(a)
#    print(b) 
#    print(c)
#    print(d)
    packet=0
    b1=2**5-1
    a=a&b1
    print("{:5:b}".format(a))


if(__name__=="__main__"):
    encrpt()
