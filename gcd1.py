def gcd(a,b):
    while(a!=b):
        if(a>b):
            return a -b
        else:
            return b-a

if(__name__=='__main__'):
    result=gcd(3,6)
    print(result)
        
    
