Class A:
    def __init__(self):
        print("Base Class constructor")

    def __del__(self):
        print("Base Destructor")



Class B(A):
    def __init__(self):
        print("First Child Constructor")



Class C(A):
    def __init__(self):
        print("Second Child Constructor")


if(__name__=="__main__"):
    A1=A()
    B1=B()
    C1=C()
    print(help(A))
    print(help(B))
    print(help(C))
    
