#14. this looks like a job for...
"""
    Instructions

First, inside your PartTimeEmployee class:

    Add a new method called full_time_wage with the arguments self and hours.
    That method should return the result of a super call to the calculate_wage method of PartTimeEmployee's parent class. Use the example above for help.

Then, after your class:

    Create an instance of the PartTimeEmployee class called milton. Don't forget to give it a name.
    Finally, print out the result of calling his full_time_wage method. You should see his wage printed out at $20.00 per hour! (That is, for 10 hours, the result should be 200.00.)

"""
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

Mishra =  Employee("Mishrajee")
print Mishra.calculate_wage(10)

milton =  PartTimeEmployee("Rambhola")
print milton.calculate_wage(15)
