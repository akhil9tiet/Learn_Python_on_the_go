
"""Read the text file which has numbers in it. What you need to do is to read the integer values and then find the sum """
import os
os.chdir('C:/Users/akhgupta/Desktop/PYTHON/Coursera_Python_for_accessing_web_data/Python for accessing web data/week1/assignment') ##setting up the working directory

import re
my_file = open("./regex_sum_263952.txt", "r")
y = re.findall('[0-9]+' , my_file.read())
y =  [int(i) for i in y]
sum1 = 0
for i in y:
    sum1 = sum1 + i
print sum1