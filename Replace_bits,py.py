def ReplaceBits(x, y, pos, n):
    temp = 2**n-1
    temp = temp<<(pos - n)
    y = y&temp
    x = x&~temp
    return x|y


if(__name__=="__main__"):
    replace=ReplaceBits(12,7,3,3)
    print(replace)
