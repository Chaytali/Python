def Isodd(num):
    return(num & 1)== 1

def main():
    lb,ub=input("Enter the lower bound & upper bound")
    
    if lb < ub:
        
            for x in range(lb,ub):
                if Isodd(x):
                    print("%d is odd" %x)
        
        
    else:
             print("Lower bound should be less than upper bound")
    

if __name__== '__main__':
    oddnum(20)
   
