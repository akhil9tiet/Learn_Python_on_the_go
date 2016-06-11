# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 01:49:25 2016

@author: akhgupta

The program will prompt 
for a URL, read the JSON 
data from that URL using 
urllib and then parse and
extract the comment counts 
from the JSON data, compute 
the sum of the numbers in the file.

"""
import json
import urllib

url = 'http://python-data.dr-chuck.net/comments_263958.json'
print 'Retrieving url=', url
uh=urllib.urlopen(url)
data = uh.read()


try:js = json.loads(data)
except:js=None
#if 'status' not in js or js['status']!= 'OK':
#    print '===Failure to retrieve==='
#    continue
print json.dumps(js, indent = 4)
print "Count:", len(js["comments"])

sum1=0
for i  in range(0,len(js["comments"])):
    sum1= sum1 + js["comments"][i]["count"]
print "Sum of count= ", sum1
    

