#12. Anonymous Function
"""Check out the code at the right. See the lambda bit? Typing

lambda x: x % 3 == 0

Is the same as

def by_three(x):
    return x % 3 == 0

Only we don't need to actually give the function a name; it does its work and returns a value without one. That's why the function the lambda creates is an anonymous function."""
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)