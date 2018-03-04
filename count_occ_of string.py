def main():
    A1=input("Enter the first string")
    A2=input("Enter the second string")
    count = 0
    Arr=[]
    Arr=A1.split(" ")
    print(Arr)
    for i in range(0,len(Arr)):
        if(A2==Arr[i]):
            count=count +1

    print("The occurence of second string is" ,count)

if(__name__ == '__main__'):
    main()
