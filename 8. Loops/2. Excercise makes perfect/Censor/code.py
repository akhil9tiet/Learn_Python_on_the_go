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