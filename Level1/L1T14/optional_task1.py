# Day 2 Project: Tip Calculator:
# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.
# Write your code below this line 

bill = input("What was the total bill? ")
bill = float(bill)

tip = input("What percentage tip would you like to give? ")
tip = float(tip)
if tip > 1:
  tip = tip /100

percantage = bill * tip
# total-bill = percantage + bill  # SyntaxError: cannot assign to expression here. It is not allowed to use a dash to
# separate words in variable names

people = input("How many people to split the bill? ")
number_of_people = people  # TypeError: unsupported operand type(s) for /: 'float' and 'str'. Need to convert "people" to an integer
# data type as the input is a string data type

# answer = round(total-bill / number_of_people, 2)

print("Each person should pay: ${answer}")  # Logical error - did not convert the string to an f-string the replace the expression
# with it's value


# RuntimeError - can't divide by zero
# x = 3
# y = 4
# z = 0
# print( x / y / z)
