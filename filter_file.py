def file1():
    count=0
    c=open('a.txt')
    filter=("Enter the filter you wish to add")
    if filter == ' ':
        while(readline(c)!= " "):
            count=count+1
        print count




if(__name__=='__main__'):
    file1()
        
