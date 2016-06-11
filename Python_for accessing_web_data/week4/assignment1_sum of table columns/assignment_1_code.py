# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 01:34:16 2016

@author: akhgupta
"""
# find all the <span> tags in the file and pull
# out the numbers from the tag and sum the numbers. 
import urllib
from BeautifulSoup import *

#url = 'http://python-data.dr-chuck.net/comments_42.html'
url = 'http://python-data.dr-chuck.net/comments_204515.html'
#raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
count = 0
sum = 0 
tags = soup('span')
for tag in tags:
   # Look at the parts of a tag
   count += 1
   sum = sum + int(tag.contents[0])

print "Count ", count
print "Sum ", sum