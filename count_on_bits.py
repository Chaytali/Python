def bin(no):
    print("{:b}".format(no))
    x=1
    count=0
    while x <=no:
        if (no & x!=0):
            count=count+1
        x=x<<1
    return(count)
            

if(__name__=="__main__"):
    result=bin(5)
    print("Count",result)
