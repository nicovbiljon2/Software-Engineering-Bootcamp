# Write a program that ask the user to enter their full name and do some validation to check if the user has entered a full name.
# If not use the appropriate error messages to inform the user to enter their full name.

# Create a variable name called "full_name"
# Request user input and store it into variable name called "full_name"
# Use the length function to get the number of characters entered by the user 
# if full_name is not equal to zero
# 	print out "You haven't entered anything. Please enter your full_name."
# elif full_name is less than 4 characters
# 	 print out "Please make sure that you have entered your name and surname."
# elif full_name is greater than 25 characters
#  	 print out "Please make sure that you have only entered your full name."
# else
# 	 print out "Thank you for entering your name."

full_name = input("Please enter your full name: ")

if len(full_name) == 0:
    print("You haven't entered anything. Please enter your full name.")
elif len(full_name) < 4:
    print("Please make sure that you have entered your name and surname.")
elif len(full_name) > 25:
    print("Please make sure that you have only entered your full name.")
else: 
    print("Thank you for entering your name.")
