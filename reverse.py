def rev():
    A=input("Enter the string")
    print(A)
    r=A[::-1]
    print("the reverse is",r)

    if(r== A):
        print("%s is a palindrome string"%A)
    else:
        print("%s is not a palindrome string"%A)
if __name__ =='__main__':
    rev()
