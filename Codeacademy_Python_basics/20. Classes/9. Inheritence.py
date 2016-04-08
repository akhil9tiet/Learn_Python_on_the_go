#9. Inheritence
"""Create a class ElectricCar that inherits from Car. Give your new class an __init__() method of that includes a "battery_type" member variable in addition to the model, color and mpg.

Then, create an electric car named "my_car" with a "molten salt" battery_type. Supply values of your choice for the other three inputs (model, color and mpg)."""

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        print "This is a %s %s with %s MPG." %(self.color, self.model, self.mpg)
    def drive_car(self):
        self.condition = "used"
class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        Car.__init__(self, model, color, mpg)
        self.battery_type = battery_type
        
my_car = ElectricCar("Volvo", "navy", 89, "molten salt")
        

