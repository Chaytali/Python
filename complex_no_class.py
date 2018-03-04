class Complex:
    def __init__(self, real=0, imaginary=0):
        
        self.Real = real
        self.Imaginary = imaginary
         
    def Add(self, real,imaginary):
        self.Real += real
        self.Imaginary +=imaginary

    def Sub(self, real,imaginary):
        self.Real -= real
        self.Imaginary -=imaginary

    def Display(self):
        print("Complex number is: %d+%di"%(self.Real,self.Imaginary))
 
if __name__=="__main__":
    c1 = Complex(10, 20)
    
    c1.Display()
    c2 = Complex(12, 24)
    c3 = Complex(1,2)
    c2.Display()
    c3.Add(10,20)
    c3.Display()
    c4 = Complex(10,5)
    c4.Sub(2,1)
    c4.Display()
