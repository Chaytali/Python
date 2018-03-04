def main():
    i=0
    count1=0
    count2=0
    A = input("Enter the string")
    length=len(A)
    print(length)
    while(i<length):
        if(A[i] in ('a','e','i','o','u')):
            count1=count1+1
            print(A[i])
        else:
            count2 = count2+1
        
        i=i+1
    print("The number of vowels",count1)
    print("The number of consonents",count2)



if(__name__== '__main__'):
    main()

        
        
    
     
