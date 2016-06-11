# remove any occurance of a vowel
def anti_vowel(text):
    string = ''
    for i in text:
        if i not in "aeiouAEIOU":
            string += i
    return string
print anti_vowel("hellouaIa world!")