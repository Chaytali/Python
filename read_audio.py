def dict1():
    a=open("a.txt")
    r=a.readlines()
    
    line2=[]
#    r=a.readlines()
    
#    while r!= " ":
    
    for line in r:
        
        line1=line.strip().split('=')
        print line1
#        line2.append(line1)
        d1=zip(line1)
                          
        


#        print(line2)
#        print(line2[1][0])
        
             
    print d1
    
#    print type(d1)
        
        
            

if(__name__=='__main__'):
    dict1()
