#17. Instantiate an Object
"""
    Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
    Print out my_triangle.number_of_sides
    Print out my_triangle.check_angles()

"""
class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180 :
            return True
        else:
            return False
my_triangle = Triangle(30, 60, 90)
print my_triangle.number_of_sides
print my_triangle.check_angles()
    