# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 21:44:11 2016

@author: akhgupta

In this assignment you will write a Python program 
somewhat similar to http://www.pythonlearn.com/code/geoxml.py. 
The program will prompt for a URL, read the XML data from 
that URL using urllib and then parse and extract the comment 
counts from the XML data, compute the sum of the numbers 
in the file and enter the sum.
"""
import urllib
import xml.etree.ElementTree as ET

url =  'http://python-data.dr-chuck.net/comments_263954.xml'
uh = urllib.urlopen(url)

data = uh.read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print counts,
sum1 = 0 
for count in counts:   
    sum1 = sum1 + int(count.text)
print sum1

#for count in counts:
#    sum1 = sum1 + count
#print "Sum= ", sum1
     