def main():
    A=input("Enter the string")
    A1=A[0:2:1]
    A2=A[-2::1]
    print(A1)
    print(A2)
    A3=(A1+A2)
    print("The new string is " ,A3)



if(__name__== '__main__'):
    main()

    
