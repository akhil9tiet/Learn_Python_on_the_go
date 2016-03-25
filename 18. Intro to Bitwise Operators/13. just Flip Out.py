# 13. just flip out
"""Using the XOR (^) operator is very useful for flipping bits. Using ^ on a bit with the number one will return a result where that bit is flipped. """
a = 0b11101110
mask = 0b11111111
print(bin(a^mask))