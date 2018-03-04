def count_alpha():
    a="aabbccddd"
    
    for i in range(len(a)):
        A=a[i]    
        
        while(i<len(a) and a[i]==A):
            print(a[i],a.count(a[i]))
            
            i=i+1
            
            if(a[i]==A):
                i=i+1
        






if(__name__=="__main__"):
    count_alpha()
