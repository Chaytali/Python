def tup():
    
    txt = 'but soft what light in yonder window breaks'
    words = txt.split()
    t = list()
    for word in words:
       t.append((len(word), word))
        
    t.sort(reverse=True)
    print(t)


if(__name__=="__main__"):
    tup()