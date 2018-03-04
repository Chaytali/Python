def sort(l1):
    n1=len(l1)
    
    

    for i in range(n1):
        for j in range(i,n1):
            if l1[j-1]>l1[j]:
                temp=l1[j-1]
                l1[j-1]=l1[j]
                l1[j]=temp

    print("After sorting",l1)           
    return(l1)

def merge(l,m):
    k=list()
    i=0
    j=0
    
    
    
    
    while i <len(l) and j < len(m):
        
        
        if l[i]< m[j]:
            k.append(l[i])
            i+=1
        else:
             k.append(m[j])
             j+=1
    
    if(i<len(l)):
        k.extend(l[i:])
    if(j<len(m)):
        k.extend(m[j:])
        
    print(k)
    
    
    
if(__name__=="__main__"):  
    l=sort([4,1,2,3])
    m=sort([8,6,5,7])
    merge(l,m)
    
