def rrotate(str1,n,st):
    while(n<=len(str1)):
        str2=str1[0:len(str1)-n]
        print(str2)
        str3=str1[len(str1)-n:]
        print("Right Rotation of the string is ",str3+str2)
#        n=n+1
        if(st in str3):
            print("Substring is present")
        else:
            print("String is not present")
        n=n+1



if(__name__=='__main__'):
    rrotate("hello",1,"he")
