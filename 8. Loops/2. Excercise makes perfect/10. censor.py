"""Instructions
Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks. 
For example:
censor("this hack is wack hack", "hack") 
should return 
"this **** is wack ****"

"""

def censor(text,word):
    new = []
    text = text.split()
    for b in text:
        if word == b:
            new.append("*" * len(b))
        else:
            new.append(b)
    return " ".join(new)
print censor("this is fuck awesome! shit fuck great!", "fuck")