def main(num):
    a=2
    b=3
    for i in range(0,1):
        
        for j in range(0,1):
            print a ,
              
        print          

    for h in range(1,num):
        for k in range(0,h+1):
            if(h==1 and k==0):
                print b ,
            else:
                b=b+2
                print b ,
        print
      
if(__name__=='__main__'):
    main(4)
