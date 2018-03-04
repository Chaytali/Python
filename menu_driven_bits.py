def OFF(x,y):
    return(x &y)

def ON(x,y):
    return(x |y)

def toggle(x,y):
    return(x ^ y)

def right(x,y):
    return(x >> y)

def left(x,y):
    return(x << y)
    

if(__name__=="__main__"):
    print("-----------Enter your choice------------")
    print("1)If you want to turn off bits")
    print("2)If you want to seton the bits")
    print("3)If you want to toggle the bits")
    print("4)If you want to right shift the bits")
    print("5)If you want to left shift the bits")     
    ch1=input("Enter the choice based on above")
    if(ch1 == 1):
          result1=OFF(3,5)
          print("The result after turning off the bits",result1)
          
    elif(ch1==2):
          result1=ON(3,5)
          print("The result after turning on the bits",result1)
          
    elif(ch1==3):
          result1=toggle(3,5)
          print("The result after turning on the bits",result1)

    elif(ch1==4):
          result1=right(3,1)
          print("The result after turning on the bits",result1)

    elif(ch1==4):
          result1=left(3,1)
          print("The result after turning on the bits",result1)

    
 
          
          
