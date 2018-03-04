def ext():
    filename = input("Input the Filename: ")
    f_extns = filename.split(".")
    #print ("The extension of the file is : " + repr(f_extns[-1]))
    print f_extns
    print type(f_extns)
    print f_extns[1]


if(__name__=='__main__'):
    ext()
