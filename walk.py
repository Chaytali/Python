import os
import sys

c=cpp=py=h=other=txt=0

def callback(arg,directory,files):
    global c
    global cpp
    global py
    global h
    global other
    global txt
    for file1 in files:

        if file1.endswith(".cpp"):
            cpp += 1

        elif file1.endswith(".py"):
            py += 1

        elif file1.endswith(".h"):
            h += 1

        elif file1.endswith(".c"):
            c += 1
        elif file1.endswith(".txt"):
            txt += 1
            
        else:
            other += 1

def main():
    print sys.argv
    os.path.walk("C:\\Python27\\Database",callback,"dir")
    print "counts are:", c,cpp,py,h,txt,other

if __name__== '__main__':
    main()
