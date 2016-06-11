"""
The number of HTTP methods you'll use is quite small—there are just four HTTP "verbs" you'll need to know! They are:

GET: retrieves information from the specified source.
POST: sends new information to the specified source.
PUT: updates existing information of the specified source.
DELETE: removes existing information from the specified source.
"""
import requests

# Make a GET request here and assign the result to kittens:
kittens= requests.get('http://placekitten.com/')

print kittens.text[559:1000]