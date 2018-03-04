def main():
    A=input("Enter the number")
    bit=input("Enter the bit to change")
    toggle= A ^ (1<<bit)
    print("{:b}".format(toggle))
    print(toggle)



if(__name__=="__main__"):
    main()




