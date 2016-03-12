"""Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result. """
def purify(numbers):
    new_numbers = []
    for i in numbers:
        if i % 2 == 0:
            new_numbers.append(i)        
    return new_numbers

print purify([4,5,5,4])

