def factorial(n):
    prod=1
    for i in range(1,n+1):
        prod = prod*i
    print(prod)


if(__name__== '__main__'):
    factorial(4)
        
