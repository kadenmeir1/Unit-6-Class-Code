"""
Name: Kaden Meir
Date:12/6/24
"""


name = "starla"
print(name.upper()) # this prints STARLA
print(name) # this prints starla - name didn't change

name = name.upper() # this will replace name with STARLA
print(name)

# lower case
name = "FRANKLIN"
print(name.lower()) # prints franklin

# title case
sentence = "FRANKLIN LEAVE MILLIE ALONE"
print(sentence.title())

# Swap case
word = "ViOlIn"
print(word.swapcase())

# strip 
school = "    Oregon State      University      "
print(school.strip())

# find: returns index of first occurence

print("Oregon State University".find("go"))


#######################################################

# Boolean checks
print("B".isupper())
print("C".islower())
print("B".isalpha())
print("B".isalnum()) # letter or number
print("B".isdigit())
