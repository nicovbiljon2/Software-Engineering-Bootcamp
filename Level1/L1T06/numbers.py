# Write a program that asked the user to enter three different numbers (integers). Then calculate the following and print out the value for each of them.
# 1. The sum of all the numbers
# 2. The first number minus the the second number
# 3. The third number multiplied by the first number
# 4. The sum of all the numbers divided by the third number

# Print out a line that ask the user to enter three different integers
# Create three variable names called "num1", "num2" and "num3"
# Store the three inputs from the user into the variable names called "num1", "num2" and "num3"
# Covert (casting) the user input to an integer by using the int function 
# Print out the total value by adding up all the numbers ("num1", "num2", "num3")
# Print out the value by minusing the first number ("num1") by the second number ("num2")
# Print out the value by multiplying the third number ("num3") by the first number ("num1")
# Print out the value by adding up all the numbers ("num1", "num2", "num3") and dividing the value of all three numbers by the third number ("num3"),
# and use the math.floor function the round the number down

import math

print("Please enter three different integers(numbers): ")

num1 = int(input("number 1: "))
num2 = int(input("number 2: "))
num3 = int(input("number 3: "))

print(num1 + num2 + num3)
print(num1 - num2)
print(num3 * num1)
print(math.floor((num1 + num2 + num3) / num3))


