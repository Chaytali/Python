def bin():
    A=input("Enter the number")
    print("{:b}".format(A))
    return(A&7== 0)


if(__name__=="__main__"):
    result=bin()
    print("Result",result)
