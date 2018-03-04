def maximum():
    A = input('Enter the 1st number:')
    B = input('Enter the 2nd number:')
    if A > B:
        print("%d The highest num than %d"%(A,B))
    else:
        print('The highest num is:' ,B)
    print("Optised max",max(A,B))


def minimum():
    A1 = input('Enter the 1st number:')
    B1 = input('Enter the 2nd number:')
    C1 = input('Enter the 3rd number:')
    print("Optimised min " ,min(A1,B1,C1))
    if(A1<B1) and (A1<C1):
            print("Smallest number is",A1)
    else :
            if(B1 <C1):
                print("Smallest number is ",B1)

            else :
                print("Smallest number is ", C1)
    




def main():
    print("Enter your choice")
    print("1.Max of 2 numbers")
    print("2.Min of 3 numbers")
    choice=input("Enter your choice")
    
    if(choice == 1):
        maximum()

    else :
        minimum()
    

main()
