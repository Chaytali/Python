def variableNumberOfDemo(*args):
    print(type(args))
    for x in args:
        print(x)

def main():
    variableNumberOfDemo(1,2,3,4)
    variableNumberOfDemo(4,5,7,9,15,20,"hi","bye")


if __name__=="__main__":

    main()
