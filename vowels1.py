def main():
    A = input("Enter the string:")
    length=len(A)
    print("Total number of character are:",length)
    i=0
    count=0
    count1=0
    while(i<length):
            if A[i]=="a" or A[i]=="e" or A[i]=="i" or A[i]=="o" or A[i]=="u":
         #   if(A[i] in ('a','e','i','o','u')):
                count=count+1
                print (A[i])
                
            else:
                count1=count1+1
                
            i=i+1
    print("the total number of vowels are :",count)
    print("The totale number of consonents are :",count1)       
            

if (__name__=='__main__'):
    main()
