def sort():
    mylist = [5, 3, 7, 2, 8, 4]
    print(mylist)
    n = len(mylist)
    for i in range(n):
        for j in range(1, n-i):
        
            if mylist[j-1] > mylist[j]:
            
                (mylist[j-1],mylist[j]) = (mylist[j],mylist[j-1])
                
    print(mylist)


if(__name__=="__main__"):
    sort()
