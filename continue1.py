def main():
    A=input("Enter the lower bound")
    B=input("Enter the upper bound")
    for i in range(A,B):
        if(i%2==0 or i%3==0):
            continue
        print(i)

if(__name__=='__main__'):
    main()
