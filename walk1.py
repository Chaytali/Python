import os

a1=input("enter the location to be walked:")
#path='C:/Users/LENOVO/Desktop/fake'
a2 = input("Enter the 2nd location to be compared:")

for root,dirs,files in os.walk(a1):
    for root1,dirs1,files1 in os.walk(a2):
        if dirs==dirs1:
            print "the files are same",dirs

   # print root
   # print dirs
    #print files
    #print ("__________")


    
    
