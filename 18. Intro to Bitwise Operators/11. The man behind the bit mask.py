# 11. The Man Behind the Bit Mask
"""A bit mask is just a variable that aids you with bitwise operations. A bit mask can help you turn specific bits on, turn others off, or just collect data from an integer about which bits are on or off.
"""
  def check_bit4(i):
    m = 0b1000
    if i & m > 0:
        return "on"
    else:
        return "off"
check_bit4(0b0)