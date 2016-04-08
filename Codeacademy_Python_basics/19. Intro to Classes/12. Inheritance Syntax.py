#12. Inheritance Syntax

"""
Create your own class, Triangle, that inherits from Shape

Inside the Triangle class, write an __init__() function that takes four arguments: self, side1, side2, and side3.

Inside the __init__() function, set self.side1 = side1, self.side2 = side2, and self.side3 = side3.
"""
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
