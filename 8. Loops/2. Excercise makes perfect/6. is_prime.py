"""to check whether the number is prime or not"""
def is_prime(x):
    if x > 0:
        if x == 0 or x == 1:
            return False
        elif x == 2:
            return True
        elif x > 2:
            for i in range(2, x-1):
                if x % i == 0 :
                    return False
            else :
                return True
    else:
        return False
print is_prime(0)
print is_prime(6)
print is_prime(11)