def maximum():
        A = input("Enter 1st number:")
        B = input("Enter 2nd number:")
        print('First number' ,A)
        print('Second number',B)
        if(A > B):
            print('Maximum number is:' ,A)
        else:
                print('Maximum number is:' ,B)

def maximun():
        A1 = input('Enter 1st number:')
        B1 = input('Enter 2nd number:')
        C1 = input('Enter 3rd number:')

        if (A1 < B1):
            if (A1 < C1):
                print('The minimun no is', A1)

            else:
                if (B1 < C1):
                    print('The minimun no is', B1)

                else:
                    print('The minimun no is', C1)


def main():

        print('Enter your choice')
        print('1 = Max number')
        print('2 = Min number')
        choice = input('Enter the choice')
        if (choice == 1):
            maximun()
        else:
            minimun()
        main()
    
    
