"""Reverse a string""""
def reverse(text):
    new_text = ''
    text_len = len(text)
    while text_len > 0:
        new_text += (text[text_len - 1])
        text_len -= 1
    else:
        str(new_text)
    return new_text
print reverse("Python!")