# Design a program for a small financial company that allows the user to access two different 
# financial calculators: an investment calculator and a home loan repayment calculator
# It must allow the user to choose which calculation they want to do.
# The first output the user should see when the program runs is as per below:

# investment - to calculate the amount of interest you'll earn on your investment
# bond       - to calculate the amount you'll have to pay on a home loan

# Enter either "investment" or "bond" from the menu above to proceed:

# The program should not be affected if the user enters capital letters or words
# If the user enters a invalid input print out an appropriate error message for the user to enter a valid input

# import math

# Create variable name called "investment"
# Print out the following message "investment - to calculate the amount of interest you'll earn on your investment"
# Create a variable name called "bond"
# Print out the following message "bond - to calculate the amount you'll have to pay on a home loan"
# add a blank line
# Create a variable name called "calculator_type"
# Print out the menu as above and request user input and store it into variable name called "calculator_type"
# Convert any capitalized letters/word to lower case word using .lower() function
# if "calculator_type" not equal to "investment" and "bond"
# 	print out error message "Invalid entry, please select one of the following options "investment or "bond": 
# 	(use the same variable name called "calculator_type" for the user to input a valid value)

# add a blank line
# If the user selects "investment"
# if "calculator_type" is equal to "investment"
# 	create a variable name called "P" and request user input. "P" is for the deposit amount. 
#   convert input value to a float data type
# 	create a variable name called "r" and request user input. "r" is for the interest entered
#   convert input value to a float data type
# 	create a variable name called "t" and request user input. "t" is for the number of years on investment
#   convert input value to a float data type
# 	create a variable name called "interest" and request user input and store it in this variable
# 		if "interest" is equal to "simple"
# 			create a variable name called "simple" to calculate the total amount when "simple" is selected
# 			convert any capitalized letters/words to lower case words using .lower() function
# 			use the following formula:
# 			simple = P * (1 + (r / 100) * t) - r divided by 100 is for the interest entered.  
# 			print out "Your total amount earned on simple interest rate of {r}% is R{simple,:.2f},
#           over a time period of {t} years." 
# 			Round  "simple" off to 2 decimals and "t" to 0 decimals
# 		elif "interest" is equal to "compound
# 			create a variable name called "compound" to calculate the total amount when "compound" is selected
# 			convert any capitalized letters/words to lower case words using .lower() function
# 			use the following formula:
# 			compound = P * math.pow((1 + (r / 100)), t) - r divided by 100 is for the interest entered
# 			print out "Your total amount earned on compound interest rate of {r} is R{compound,:.2f},
#           over a time period of {t:.0f} years." 
# 			Round "compound" off to 2 decimals and "t" to 0 decimals
# 		elif "interest" is not equal to "simple" and not equal to "compound"
# 			create a variable name called "simple" to calculate the total amount when "simple" is not selected
# 			use the following formula:
# 			simple = P * (1 + (r / 100) * t) - r divided by 100 is for the interest entered.
# 			print out "Your total amount earned on simple interest rate of {r}% is R{simple,:.2f},
#           over a time period of {t} years."
# 			Round  "simple" off to 2 decimals and "t" to 0 decimals
# 			create a variable name called "compound" to calculate the total amount when "compound" is not selected
# 			use the following formula:
# 			compound = P * math.pow((1 + (r / 100)), t) - r divided by 100 is for the interest entered
# 			print out "Your total amount earned on compound interest rate of {r} is R{compound,:.2f},
#           over a time period of {t:.0f} years." 
# 			Round "compound" off to 2 decimals and "t" to 0 decimals

# add a blank line	
# If the user selects "bond"
# if calculator_type is equal to "bond"
# 	create a variable name called "P" and request user input. "P" is the present value of the house. 
#   convert input value to a float data type
# 	create a variable name called "i" and request user input. "i" is the monthly interest rate. 
#   convert input value to a float data type
# 	create a variable name called "n" and request user input. "n" is the number of months the bond will be paid over.
#   convert input value to a float data type
# 	calculate the interest rate for variable name "i" by dividing "i" by hundred and,
#   then divide the answer by 12(number of months per year)
# 	create a variable name called "repayment" to calculate the user monthly repayments
# 	use the following formula:
# 	repayment = (i * P) / (1 - (1 + i) ** (-n))
# 	print out "Your total monthly repayment is R{repayment:.2F}."
#   round "repayment" off to 2 decimals

import math

investment = print("investment - to calculate the amount of interest you'll earn on your investment")
bond = print("bond\t   - to calculate the amount you'll have to pay on a home loan")

print()

calculator_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if calculator_type != "investment" and calculator_type != "bond":
    calculator_type = input("Invalid Entry, please select one of the following options 'investment' or 'bond': ").lower()

print()
# if the user selects "investments"

if calculator_type == "investment":
    P = float(input("Please enter deposit amount: "))
    r = float(input("Please enter the interest rate: "))
    t = float(input("Please enter planned number of years to invest: "))
    interest = input("Please select interest type 'simple' or 'compound': ").lower()
    
    if interest == "simple":
        simple = P * (1 + ((r / 100) * t))
        print(f"Your total amount earned on simple interest rate of {r}% is R{simple:.2f} over a period of {t:.0f} years.")
    elif interest == "compound":
        compound = P * math.pow((1 + (r / 100)), t)
        print(f"Your total amount earend on a compound interest rate {r}% is R{compound:.2f} over a period of {t:.0f} years.")
    elif interest != "simple" and interest != "compound":
        simple = P * (1 + ((r / 100) * t))
        print(f"Your total amount earned on simple interest rate of {r}% is R{simple:.2f} over a period of {t:.0f} years.")
        compound = P * math.pow((1 + (r / 100)), t)
        print(f"Your total amount earend on a compound interest rate {r}% is R{compound:.2f} over a period of {t:.0f} years.")

print()
# if user selects bond:

if calculator_type == "bond":
    P = float(input("Please enter the present value of the property: "))
    i = float(input("Please enter the interest rate: "))
    n = float(input("Please enter the repayment period(months) for the bond: "))
    i = ((i / 100) / 12)
    repayment = (i * P) / (1 - (1 + i) ** (-n))
    print(f"Your total monthly repayment on the bond is R{repayment:.2f}.")