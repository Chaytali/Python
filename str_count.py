def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
            print(str1.index(n))
        else:
            dict[n] = 1
    return dict




if(__name__=="__main__"):
    char1=char_frequency('google.com')
    print char1
