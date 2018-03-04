def dict1():
    d = {}
    f = open('a.txt', 'r')
    for line in f.readlines():
        name,score = line.split("=")
        d=[name][score]

    print d


if(__name__=='__main__'):
   dict1()
