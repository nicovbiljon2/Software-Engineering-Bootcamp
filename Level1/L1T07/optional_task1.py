# Write a program that asked the user to enter a number and to test whether the number is odd or even number.

# Create a variable name called "number"
# Request user input and store it into variable name called "number" and convert the input to an integer data type value 
# if the remainder of the number two equals to zero
#	 print out "Even"
# else
# 	 print out "Odd"

number = int(input("Please enter a number: "))

if number % 2 == 0:
    print(F"{number} is Even")
else:
    print(f"{number} is Odd")
    
