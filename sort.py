def sort():
    l1=[8,4,10,1]
    l=len(l1)-1
    print l
    
    for i in range(l):
        if( l1[i] > l1[i+1]):
                temp = l1[i]
                l1[i]=l1[i+1]
                l1[i+1]=temp
                
        
    
        print(i)
    print l1


if(__name__=="__main__"):
    sort()
