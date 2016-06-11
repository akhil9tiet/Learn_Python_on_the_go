#Database access functions for the web forum
# we can even use single quotes
#however we cannot put random javascript code as comments yet, as it throws spam alerts
#bleach library will be used to protect spamming when javascript code is entered


import psycopg2
## Get posts from database.
def GetAllPosts():
    DB= psycopg2.connect("dbname=forum")
    c= DB.cursor()
    c.execute("SELECT time, content FROM posts ORDER BY time DESC")
    posts = ({'content': str(row[1]), 'time':str(row[0])} for row in c.fetchall())
    DB.close()
    return posts

## Add posts to database
def Addpost(content):
    DB= psycopg2.connect("dbname=forum")
    c= DB.cursor
    c.execute("INSERT INTO posts (content) VALUES (%s)", (content,))
    DB.commit()
    DB.close()