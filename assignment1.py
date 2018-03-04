def line():
    f=open("b.txt")
    count=count1=c3=0
    filter=input("Enter the filter")
    print filter
    if(filter==""):
        for line in f:
            count+=1
        print("The total lines in the file are",count)

    elif(filter=="^This"):
        a=filter.split('^')
        print a[1]
        b=str(a[1])
        print b
        
        for line in f:
            if(line.startswith(b)):
                count1=count1+1
        print("The count of lines starting with given filter",count1)

    elif(filter=="$this"):
        a1=filter.split("$")
        print a1
        b1=str(a1[1])
        print b1,type(b1)
        for line in f:
            print type(line)
            if(line.endswith("this")):
                c3=c3+1
        print("The count of lines ending with this are",c3)
        
        
if(__name__=='__main__'):
    line()
