"""
Check out the code in the editor. We've imported xml.dom.minidom from the xml module for parsing XML, and we're just using the open() method to read from pets.txt (under the "Files") tab. Reading from this file is just like reading XML sent by a server.
"""
from xml.dom import minidom

f = open('pets.txt', 'r')
pets = minidom.parseString(f.read())
f.close()

names = pets.getElementsByTagName('name')
for name in names:
	print name.firstChild.nodeValue