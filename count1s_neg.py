def bin(no):
    print("{:b}".format(no))
    mask=1
    count=0
    test=1
    test1=111
    result= (no ^ test1 ) + 1
    print("{:b}".format(result))
    print(result)

    while(result!=0):
        if(result & mask != 0):
            count+=1
            result>>test
        test+=1
    print(count)


if(__name__=="__main__"):
    result=bin(6)
