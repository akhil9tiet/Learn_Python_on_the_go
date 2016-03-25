#3. Writing
"""

    Iterate over my_list to get each value
    Use my_file.write() to write each value to output.txt
    Make sure to call str() on the iterating data so .write() will accept it
    Make sure to add a newline ("\n") after each element to ensure each will appear on its own line.
    Use my_file.close() to close the file when you're done.
"""
my_list = [i**2 for i in range(1,11)]
print my_list

my_file = open("output.txt", "w+")

# Add your code below!
"""Iterate over my_list to get each value"""
for x in my_list:
    my_file.write(str(x)+ "\n")
my_file.close()
