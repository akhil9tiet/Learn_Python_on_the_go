#9. Case Closed
"""
Below your with...as code, do two things:

    Check if the file is not .closed.
    If that's the case, call .close() on it.
    (You don't need an else here, since your if statement should do nothing if .closed is True.)
    After your if statement, print out the value of my_file.closed to make sure your file is really closed.
"""
with open("text.txt", "w") as my_file:
    my_file.write("jiea")
#!== is not a valid comparator in python
#!= is the correct comparator
if my_file.closed != True:
    # you called return here remember
    #you can only call return inside a function
    my_file.close()
print (my_file.closed)