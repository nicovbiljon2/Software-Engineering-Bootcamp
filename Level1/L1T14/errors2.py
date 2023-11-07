# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"  # SyntaxError - no quotes around the string
animal_type = "cub"
number_of_teeth = 16

full_spec = (f"This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth")  # Logical Error - didn't change it to an f-string to replace the expressions with their values. 
# The string should also be inside parentheses.
print(full_spec)
