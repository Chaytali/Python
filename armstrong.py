def main():
    A=input("Enter the number from the user")
    A1=A
    sum=0
    while(A1>0):
        A2=A1%10
        sum=sum+ (A2*A2*A2)
        A1=A1/10
    print(sum)
    if(sum==A):
        print("The number is armtrong number")

if(__name__=='__main__'):
    main()
