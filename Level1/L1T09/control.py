# Write a program that asked the user to enter their age to check if they are over 18 or older,
# or almost 18 or too young.

# Create a variable name called "age"
# Request user input and store it into variable name "age". Convert the data type to an integer data type

# if the user's age is greater than 18 or equal to 18
# 	print put "You are old enough" 
# elif the user's age is equal or over 16 and less than 18
# 	print out "Almost there"
# else
# 	print out "You're just too young"


age = int(input("Please enter your age: "))

if age >= 18:
    print("You are old enough")
elif age == 17:
    print("Almost there")
else:
    print("You're just too young")




