def isempty(l1):
    if(l1== []):
        print("Queue is empty")
    else:
        print("Queue is not empty")

def isfull(l1):
    if(len(l1)== 7):
        print("Queue if full")
        return 0
    else:
        print("Queue is not yet full")
        return 1

def push(l1,y):
    x1=isfull(l1)
    
    if(x1==0):
        print("Queue is full cannot enter new element")
    else:
        l1.append(y)
        print("After adding the new element",l1)


def pop(l1):
    print(l1.pop(0))
    print("The stack after removing the element",l1)


if(__name__== "__main__"):

    n=3
    while(n>0):
        
        print("\nStack Operations")
        print("\n1.If you want to insert in the queue")
        print("\n2.If you want to remove the item from queue")
        print("\n3.Check if queue is full")
        print("\n4.Check if queue is empty")
    
        x=input("\nEnter ur selection")
        l1=[1,2,3,4]
        print l1
        if(x==2):
            print(pop(l1))
        elif(x==1):
            y=input("Enter the elemet you wish to insert")
            push(l1,y)
        elif(x==3):
            isfull(l1)
        elif(x==4):
            isempty(l1)
        n-=1
        
