def bin(a):
    if(a>1):
#        print a%2 ,
        bin(a/2)

    print a%2 ,


if(__name__=='__main__'):
    bin(8)
    
