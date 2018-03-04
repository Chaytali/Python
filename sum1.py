def main():
    A[]=input("Enter the numbers")
    sum=0
    for i in range(0,len(A)):
        sum=sum+A[i]

    print("The sum of %d is %d" % len(A),sum)



if(__name__=='__main__'):
    main()
