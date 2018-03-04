def add(N1,N2):
    N3=N1+N2
    print("Addition of 2 nos",N3)

def sub(N1,N2):
    N3=N1-N2
    print("Subtraction of 2 nos",N3)


def mul(N1,N2):
    N3=N1*N2
    print("Multiplication of 2 nos",N3)

def div(N1,N2):
    N3=N1/N2
    print("Division of 2 nos",N3)





def main():

        print('Enter your choice')
        print('1 = Addition of the number')
        print('2 = Subtraction of number')
        print('3 = Multiplication of number')
        print('4 = Division of number')
        N1=input("Enter the first number")
        N2=input("Enter the second number")
        choice = input('Enter the choice')
        if (choice == 1):
            add(N1,N2)
        elif(choice == 2):
            sub(N1,N2)
        elif(choice == 3):
            mul(N1,N2)
        elif(choice == 4):
            div(N1,N2)
        


if(__name__ == '__main__'):
    main()

