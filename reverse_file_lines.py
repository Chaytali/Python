def reverse():
    f=open("b.txt")
    for line in f:
        words = line.split()
        sentence_rev = " ".join(reversed(words))
        print sentence_rev


if(__name__=='__main__'):
    reverse()
