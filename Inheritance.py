class A:
    def __init__(self,name):
        print("Base Class constructor")

    def __del__(self):
        print("Base Destructor")



class B(A):
    def __init__(self,name):
        print("Child1 Class constructor")
    
 
    

class C(A):
    def __init__(self,name):
        print("Second Child Constructor")



class D(B,C):
    pass


if(__name__=="__main__"):
    A1=A("Chaytali")
    B1=B("ABC")
    C1=C("XYZ")
    D1=D("MNO")
    print(help(A))
    print(help(B))
    print(help(C))
    print(help(D))
    
