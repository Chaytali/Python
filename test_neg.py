def main():
    A=input("Enter the number")
    count=0
    rev= (A ^ 7) +1
    print("{0:b}".format(rev))
    print(rev)
    while(rev):
        if(rev & 1 !=0):
            count+=1
        rev>>=1
    
    print(count)   
if(__name__=="__main__"):
    main()





    
