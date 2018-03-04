def Factorial(number):
    fact = 1
    for i in range(2, number+1):
        fact = fact*i
    return fact




def IsSpecial(number):
    sum_of_fact = 0
    original_number = number
    while number != 0:
        digit = number % 10
        sum_of_fact += Factorial(digit)
        number = number / 10
 
    return original_number == sum_of_fact


if(__name__=='__main__'):
    a=IsSpecial(145)
    print a
    if(a):
        print("The number is a special number")
    else:
        print("The number is not a special number")
