class complex1:

    def __init__(self,real,img):
        self.real=real
        self.img=img

    def add(self,real,img):
        self.real+=real
        self.img+=img

    def sub(self,real,img):
        self.real-=real
        self.img-=img
        
    def display(self):
        print("the complex num are: %d  %di",(self.real,self.img))

if __name__=='__main__':
    x=complex1(10,20)
    x.add(1,2)
    x.display()
        
