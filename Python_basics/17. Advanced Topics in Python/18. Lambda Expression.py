# 18. Lambda Expressions

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
"""

    Create a new variable called message.
    Set it to the result of calling filter() with the appropriate lambda that will filter out the "X"s. The second argument will be garbled.
    Finally, print your message to the console.
"""
message = filter(lambda x: x!= 'X', garbled)
print message

