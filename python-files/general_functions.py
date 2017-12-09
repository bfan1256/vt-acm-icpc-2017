def factorial(number):
    '''computes factorial'''
    result = 1
    for i in range(1, number):
        result *= i
    return result
