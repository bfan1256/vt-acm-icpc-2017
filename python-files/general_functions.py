def factorial(number):
    '''computes factorial'''
    result = 1
    for i in range(1, number+ 1):
        result *= i
    return result

def sumPascalRow(n):
    return 2**n
def nthPascalValue(n):
    '''NOTE IMPORT FACTORIAL WITH THIS FUNCTION'''
    numbers = 1
    start = 1
    while n > numbers:
        start += 1
        numbers += start
    index = numbers - n
    value = factorial(start - 1) / (factorial(index)
                                    * factorial(start - 1 - index))
    return value
