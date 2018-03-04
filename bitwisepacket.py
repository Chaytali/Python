def packet(version,a,b):

    p1=version
    p1= p1<<1
    p1= p1 | a
    p1= p1<<2
    p1= p1 | b
    
    return p1

if __name__=='__main__':
    a=packet(4,1,4)
    print a
