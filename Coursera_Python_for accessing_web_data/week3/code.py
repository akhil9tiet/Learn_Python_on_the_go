"""In this assignment you write a Python program to retrieve a web page over a socket and display the headers from the web server."""
import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysocket.connect(('www.py4inf.com', 80))
mysocket.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysocket.recv(512)
    if (len(data) < 1):
        break
    print data
mysocket.close()