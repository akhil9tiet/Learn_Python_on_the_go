#7. The 'with' and 'as' keywords
"""'with' and 'as' keywords are used to automatically close the file without explicitly closing them"""
with open("text.txt", "w") as textfile:
	textfile.write("Success!")

