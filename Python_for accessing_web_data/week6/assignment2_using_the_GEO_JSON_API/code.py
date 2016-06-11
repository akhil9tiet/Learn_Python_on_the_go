# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 12:10:17 2016

@author: akhgupta
"""
import urllib
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    js = json.loads(str(data))

    location = js['results'][0]['place_id']
    print "Place id:", location

