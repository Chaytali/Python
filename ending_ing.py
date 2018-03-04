def main():
    A=input("Enter the string")
    B="ing"
    C= "ly"
#    if(len(A)==3):
#        print("The new string is ",A)
#    elif(len(A)>3):
#         print("The string is as it is",A+B)
    if(A.endswith(B)):
         print("The new string",A.replace(B,C))
    else:
        print("The new string is ", A)


if(__name__=='__main__'):
    main()
