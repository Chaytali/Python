def main():
    A=input("Enter the first string")
    B=input("Enter the second string")
    A1=A[0:2:1]
    print(A1)
    B1=B[0:2:1]
    print(B1)
    print("The new first string " ,B1+A[2:len(A):1])
    print("The nee second string ",A1+B[2:len(B):1]) 


if(__name__ == '__main__'):
    main()
