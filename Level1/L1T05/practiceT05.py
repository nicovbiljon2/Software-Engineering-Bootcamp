# Examples of strings
# name = "Linda"
# song = "The bird song"
# license_plate = "CTA 456 GP"
# telephone_num = "041 1231234"

# Example of multi-line string
# long_string = ''' This is a long string
# using triple quotes preserves everything inside it as a string
# even on different lines and with different \n spacing. '''

# Concatenation of strings
name = "Peter"
surname = "Parker"
full_name = name + " " + surname

print(full_name)
print(full_name +  " " + str(32))

name1 = "Tim"
sentence1 = "My name is"
print(sentence1 + " "+ name1)

# formatting a string using the .format() method
name = "Peter Parker"
age = 32
sentence = "My name is {} and I'm {} years old.".format(name, age)
# The f-sting fromat function
sentence1 = f"My name is {name} and I'm {age} years old."

print(sentence)
print(sentence1)

# each character of a string
greeting = "Hello"
print(greeting[0] + greeting[1] + greeting[2] + greeting[3] + greeting[4])

# print the length of a string
print(len("Hello World!"))

# slicing a string
greeting = "Hello"
print(greeting[1:4])
print(greeting[1:])
print(greeting[:1])
print(greeting[1::2])
print(greeting[4:1:-1])
print(greeting[::-1])

print()

new_string = "Hello world!"
fizz = new_string[0:5]
print(fizz)
print(new_string)

print()

# handeling string functions 
a_string = "Hello World!"

print(a_string.upper()) 
print(a_string.lower())

a_sentence = "Welcome$to$the$world$of$prgramming"
print(a_sentence.replace("$", " "))

str_help = "******Please leave me alone******"
print(str_help.strip("*"))

print()

# Example 1 - additional examples of stings
print("Example 1: ")

name = "Joe Black"
fact = "A traffic jam that lasted for more than 10 days, with cars only moving 0.6 miles a day."
address = "150 Crossvender Avenue"
empty_str = ""

print(name)
print(fact)
print(address)
print(empty_str)

print()

# example 2 - indexing of strings
print("Example 2: ")

word = "Hello"
# indexing from 0 to 4
char1 = word[0]
char2 = word[1]
char3 = word[2]
char4 = word[3]
char5 = word[4]
print(char1)
print(char2)
print(char3)
print(char4)
print(char5)

# indexing from -5 to -1
char1 = word[-1]
char2 = word[-2]
char3 = word[-3]
char4 = word[-4]
char5 = word[-5]
print(char1)
print(char2)
print(char3)
print(char4)
print(char5)

print()

# more examples of slicing a string
print("Example 3: ")

very_long_word = "supercalifragilisticexpialidocious"
print(very_long_word[0:5])

# Example 4:
index = 6
print(very_long_word[index:9])

# Example 5:
print(very_long_word[0:])
print(very_long_word[:])
print(very_long_word[:9])
