
def main():
    a=open("a.txt")
    d={}
    line=a.readline()
    while(line!=""):
        print line
        sp=line.split('=')
        print sp
        line=a.readline()
        d=sp
        

    print (d) 
    
    

        
if(__name__=="__main__"):
    main()
        
