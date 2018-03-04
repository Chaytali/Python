def main():
    A=input("Enter the number of rows")
    k=2*A-1
    for i in range(0,A):
        for j in range(0,k):
            print " " ,
        k=k-1   
        for l in range(0,i+1):
            print chr(65+i) ,
            
        print

if(__name__ == '__main__'):
    main()
