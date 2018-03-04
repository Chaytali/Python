import collections
def main():
    a="aabbbcccdddd"
    for i in range (0,len(a)):
        
        result=collections.Counter(a[i])
        print(result,i)



if(__name__=="__main__"):
    main()
