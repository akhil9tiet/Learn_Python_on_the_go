# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:01:28 2016

@author: akhgupta
4. RETful API

Check out the code in the editor. 
This is a call to the PlaceKitten API. 
Click Save & Submit Code to see what it does!

"""

from urllib2 import urlopen

kittens = urlopen('http://placekitten.com/200/300')

f = open('kittens.jpg', 'wb')
f.write(kittens.read())
f.close()