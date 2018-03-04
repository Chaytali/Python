def traingle():
    sideA = input("Enter the first side of traingle")
    sideB = input("Enter the second side of traingle")
    sideC = input("Enter the third side of traingle")
    sq=(sideA*sideA)+(sideB*sideB)
    print("The sum of squares of first 2 sides are",sq)
    sq1=sideC*sideC
    print("The square of the third side is",sq1)
    if(sq >= sq1):
        print("A traingle can be formed with all 3 numbers entered")
    else:
        print("A traingle cannot be formed with all 3 numbers entered")

traingle()
