def gcd(a,b):
    if b == 0:
        print a
    else:
        return gcd(b, a%b)
      


if(__name__=='__main__'):
    gcd(4,6)
