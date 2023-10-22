# Write a program that ask the user to enter his/her year of birth to see if they are 18 or older to be allowed entry into a party

# Create a variable name called "year_born"
# Request user input and store it into variable name called "year_born" and convert the input to an intgeter data type
# Create another variable name called "current_year" and assign the value of "2023" to this variable name. 
# Create another variable name called "age" and calculate the user age by minusing variable name "current_year" by "year_born"
# if the user's age is greater than or equal to 18
#	 print out "Congrats you are old enough"
# else
# 	 print out "Sorry you are not old enough"

year_born = int(input("Please enter your year of birth: "))
current_year = 2023
age = current_year - year_born

if age >= 18:
    print("Congrats you are old enough")
else:
    print("Sorry you are not old enough")

