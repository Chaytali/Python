class Student:
    def __init__(self,value):
        print id(self)
        self.object_attribute=value
        print("In Constuctor")


    def __del__(self):
        print("In Destructor")

    def setAttribute(self,value):
        
        self.object_attribute=value

    def getAttribute(self):
        
        return self.object_attribute
        



if(__name__=="__main__"):
    x=Student(10)
    y=Student(20)
    print(x.getAttribute())
    print(y.getAttribute())
    print id(x)
    print id(y)
    print(x.__dict__)
    print(y.__dict__)
    
