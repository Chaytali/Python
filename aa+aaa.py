def pattern():
    N = 5
    DIGIT = 5
    s = 0
    for i in range(1,DIGIT+1):
        s += int(str(N)*i) 
        print s



if(__name__=='__main__'):
    pattern()
