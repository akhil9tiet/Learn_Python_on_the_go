""""Find factorial of a number"""
ef factorial(x):
    l = x
    fact = 1
    while l >= 1:
        fact = fact * l
        l = l - 1
    return fact
print factorial(3)
print factorial(5)        