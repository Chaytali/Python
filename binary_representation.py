def bin():
    A=input("Enter the number")
    print("Decimal of the number",A)
    C='1010'
    print int('101',2)
    print("Binary of the number ","{0:b}".format(A))
    B=input("Enter the number of the bit to OFF")
    
    #print("{:b}".format(1<<A),"{:d}".format(1<<A))
    print("{:b}".format((A and 1<<B-1)))
    print("{:b}".format(C & 0010 )==0010)
    
   

if(__name__=="__main__"):
    bin()
