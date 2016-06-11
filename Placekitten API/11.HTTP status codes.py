# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:16:23 2016

@author: akhgupta
"""

"""
A successful request to the server results in a response, which is the message the server sends back to you, the client.

The response from the server will contain a three-digit status code. These codes can start with a 1, 2, 3, 4, or 5, and each set of codes means something different. (You can read the full list here). They work like this:

1xx: You won't see these a lot. The server is saying, "Got it! I'm working on your request."

2xx: These mean "okay!" The server sends these when it's successfully responding to your request.

3xx: These mean "I can do what you want, but I have to do something else first." You might see this if a website has changed addresses and you're using the old one; the server might have to reroute the request before it can get you the resource you asked for.

4xx: These mean you probably made a mistake. The most famous is "404," meaning "file not found": you asked for a resource or web page that doesn't exist.

5xx: These mean the server goofed up and can't successfully respond to your request.
"""
import requests

response = requests.get('http://placekitten.com/')

# Add your code below!
"""
Get the status_code attribute of the response object on line 6. print this value so you can see the status code returned by the server. It should be '200', standing for OK!
"""
print response.status_code()