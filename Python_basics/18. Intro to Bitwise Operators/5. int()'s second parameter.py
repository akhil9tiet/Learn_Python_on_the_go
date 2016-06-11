#5. int()'s second parameter
"""What you might not know is that the int function actually has an optional second parameter.

int("110", 2)
# ==> 6

When given a string containing a number and the base that number is in, the function will return the value of that number converted to base ten."""
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("0b11001001",2)