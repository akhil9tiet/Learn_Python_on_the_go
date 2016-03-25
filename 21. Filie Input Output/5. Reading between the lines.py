#5.Reading between the Lines
"""
We need to check if the file we are going to read from is available or not, if not then we create it

    Declare a new variable my_file and store the result of calling open() on the "text.txt" file in "r"ead-only mode.
    On three separate lines, print out the result of calling my_file.readline(). See how it gets the next line each time?
    Don't forget to close() your file when you're done with it!)

"""
import os
print "==show us the existing files =="
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print str(f)
#my_file.close()
print "== if the file doesn't exist, create one =="
if os.path.exists('text.txt'):
    print "File exists"
else:
    print "Creating the text.txt-file"
    my_file = open("text.txt", 'w')
    my_file.write("I'm the first line of the file!" +"\n")
    my_file.write("I'm the second line."+"\n")
    my_file.write("Third line here, boss."+"\n")
    my_file.close()
    
my_file = open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()