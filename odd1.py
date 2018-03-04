def main():
    A1=input("Enter the lower limit")
    A2=input("Enter the upper limit")
    N=A1
    for N in range(A1,A2):
        if(N%2 == 1):
            print(N)
        N=A1+1
            


if(__name__=='__main__'):
    main()
