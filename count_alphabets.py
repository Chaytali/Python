import collections
def count_alphabets():
    a="aabbccddd"
    b={1:"name",2:"age",3:"address"}
    result=collections.Counter(a)
    print(result)
    print(b.items())


def charcount(input_str):
    result_dict={}
    i=0
    while i < len(input_str):
        if(result_dict.has_keys(input_str[i])):
            result_dict[input_str[i]]=result_dict[input_str[i]]+1
        else:
            result_dict[input_str[i]]=1
    
        i=i+1


if(__name__=="__main__"):
    count_alphabets()
    charcount("aabbccddd")
    
    
