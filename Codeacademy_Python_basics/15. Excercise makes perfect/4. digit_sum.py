#sum the digits of a number
def digit_sum(n):
    x = str(n)
    sum = 0
    for i in range(0,len(x)):
        sum = sum + int(x[i])
    return sum

print digit_sum(124)
print digit_sum(111)
print digit_sum(201)

