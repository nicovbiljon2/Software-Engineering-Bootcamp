# Write a program that continually asks the user to enter a number.
# If the user enters -1 the program should stop requesting the user the enter a number.
# The program must then calculate the average of the numbers entered, excluding the -1.

# Create a variable name called "numbers" and assign a value of zero to this variable
# Create a variable name called "count" and assign a value of zero to this variable
# Create a variable name called "user_input" 
# Request user input and store it into variable name "user_input". Convert input value to a float data type
# While True
# 	request user to enter a number or minus one to exit the program
	
# 	if "numbers" is equal to minus one
# 		print out "The total number is {numbers}."
# 		break out of the while loop
# 	"numbers" plus equals(+=) "user_input" - this is to add up all the number the user have entered to get the total
# 	"count" plus equals(+=) one - this is to add up all the inputs the user made
			
# Create a variable name called "average_number" to calculate the average of the total numbers entered by the user
# divide "numbers" by "count" to get the average of all the numbers entered
# Print out "The average of all the numbers entered is {average_number:.2f} and round it off to 2 decimals

numbers = 0
count = 0

while True:
    user_input = float(input("Please enter a number (enter -1 to exit): "))
    
    if user_input == -1:
       print(f"The total number entered is {numbers}.")
       break
    numbers += user_input
    count += 1
       
average_number = numbers / count
print(f"The average of all the numbers entered is {average_number:.2f}.")







