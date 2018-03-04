def main():
    A = input("Enter the string")
    B=[]
    n=0
    i=0
    B=A.split(" ")
    print(B)
    for i in range(0,len(B)):
        n=n+1
#    print("Count of words",n)
    
    for i in range(0,len(A)):
        i=i+1
    print("Count of words",n)
    print("Count of alphabets",i)
    print("Total count of alphabets and words",i+n)

if(__name__ == '__main__'):
    main()
