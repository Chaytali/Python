def alternate():
    f=open("b.txt").read()
    print type(f)
    n = 0
    s = 2
    m = len(f)
    print m

    while n < m :
        f.seek(n)
        a=f.read(s)
        print a
        n =+ 2
        

    
    
    

if(__name__=="__main__"):
    alternate()
