# Write a program that ask the user to enter his favourite restaurant as well as his favourite number. 
# Print out both statements on separate lines.

# Create a variable name called "string_fav"
# Request user input and store the value into variable name "string_fav"
# Create another variable name called "int_fav"
# Request user input and store the value into variable name"int_fav"
# Print out both statements on separate lines
# Try to cast variable name "string_fav" to an integer

string_fav = input("Please enter your favourite resturant: ")

int_fav = input("Please enter your favourite number: ")

print(string_fav)
print(int(int_fav))

# Try to cast sting_fav to an integer
print(int(string_fav))
# Result:
# ValueError: invalid literal for int() with base 10: 'tin cap'
# My explanation:
# The reason for the error is that you cannot convert characters / letters into integers (numbers) as they are non-numeric values. 
