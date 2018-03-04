import re
def reg1():
    a="Regular Expression"
    i=0
    l1=[]
    b=re.search("e",a)
    print(b.start())
    t= b.start()
    print("Position",t)
    l1.append(t)
    print(l1)
    x=b.end()
    print(a[x::])

    c=re.search("e",a[x::])
    t1=c.start()
    print t1

    l1.append(t1+x+t)

    
    

    
   
    
if(__name__=="__main__"):
    reg1()
