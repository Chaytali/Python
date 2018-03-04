def dec(a):
    i=0
    B=0
    while(a!=0):
        
        A=a%10
        
        B=B+A*pow(2,i)
        a=(a/10)
        
        i=i+1
        
    print(B)

if(__name__=='__main__'):
    dec(100)

