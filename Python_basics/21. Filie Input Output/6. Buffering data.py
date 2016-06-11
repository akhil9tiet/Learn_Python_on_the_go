#6. PSA: Buffering data
"""Check out our extremely bad code in the editor. Click Save & Submit Code—you'll note that our read_file.read() didn't read any data back! (The text still appears in text.txt, though, because we closed the file behind the scenes for you. Safety first!)

    Add a write_file.close() call on line 9.
    Add a read_file.close() on line 13."""
# Open the file for reading
read_file = open("text.txt", "r")

# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")
# Write to the file
write_file.write("Not closing files is VERY BAD.")

write_file.close()

# Try to read from the file
print read_file.read()
read_file.close()