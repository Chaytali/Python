def main():
    import glob
    import os
    
    
    
    a2=glob.glob("C:/Users/LENOVO/Desktop/fake/*txt")
    print a2
    for f1 in a2:
        print f1
        os.remove(f1)



if(__name__=="__main__"):
   main()




