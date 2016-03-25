#2. Keys() and Values() 
"""For iterating over lists, tuples, dictionaries, and strings, Python also includes a special keyword: in. You can use in very intuitively, like so:

for number in range(5):
    print number,

d = { "name": "Eric", "age": 26 }
for key in d:
    print key, d[key],

for letter in "Eric":
    print letter,  # note the comma!

In the example above, first we create and iterate through a range, printing out 0 1 2 3 4. Note that the trailing comma ensures that we keep printing on the same line.

Next, we create a dictionary and iterate through, printing out age 26 name Eric. Dictionaries have no specific order.

Finally, we iterate through the letters of a string, printing out E r i c."""

my_dict = {
            'Name': 'Awesone',
            'Age':69,
            'BDSM': True
          }
for k in my_dict:
    print k, " ", my_dict[k]
