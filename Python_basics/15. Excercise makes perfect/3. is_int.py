"""Check whether the given number is an integer or not"""
def is_int (x):
    l = float (x)
    l = l*10
    if l%10 == 0:
        return True
    else:
        return False
        
print is_int(7.5)
print is_int(7.0)
print is_int(1)
