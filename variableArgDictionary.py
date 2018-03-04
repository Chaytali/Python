def variableArgsDicDemo(a,b,c,*args,**kwargs):

    print(a,b,c)
    print(type(args))
    for x in args:
        print(x)
    print(type(kwargs))
   # for key in kwargs:
    for key,value in kwargs.items():
        print(key,kwargs[key])
   #     print(key,value)
def main():
    variableArgsDicDemo(1,2,3,7,8,9,10,"ABC","XYZ",name="aniket",hobby="fitness")
    
if __name__=='__main__':
    main()
