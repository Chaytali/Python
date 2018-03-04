def file1():
    a=open("b.txt")
    line=a.readlines()
    print(type(line))
    print(line[0:2])
    
        
#    print list(a)


if(__name__=="__main__"):
    file1()
