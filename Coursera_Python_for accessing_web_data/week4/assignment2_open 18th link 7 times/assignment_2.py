# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 01:14:09 2016

@author: akhgupta
"""

#Find the link at position 18 (the first name is 1). 
#Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
import urllib
from BeautifulSoup import *
url= 'http://python-data.dr-chuck.net/known_by_Brandon.html'

#open 18th link 7 times
count = 1

while count <= 7:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    #print tags,
    count = count + 1
    url = tags[17].get('href', None)
    print 'Retrieving: ', url,
    
print
print 'Last url:', tags[17]
