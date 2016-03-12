#Return product of all elements in a list
def product(lst):
    prod = 1
    for i in lst:
        prod *= i
    return prod
print product([4,5,5])
    