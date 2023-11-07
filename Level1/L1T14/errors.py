# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")  # SyntaxError - missing the parentheses
print("\n")  # SyntaxError - incorrect indentation. Should be inline fir the first print function. It also misses the parentheses

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old."  # IndentationError - incorrect indentation and NameError: name 'age_Str' is not defined. The NameError is caused by the "==" double equal sign.
age = (age_Str)  # IndentationError - incorrect indentation and ValueError: invalid literal for int(). Can't convert letters to integers 
print("I'm" + " " + age)  # IndentationError - incorrect indentation and SyntaxError - The message does not have the appropriate spacing - require: + " " +. "years old." needs to be removed as it prints twice.                        

# Variables declaring additional years and printing the total years of age
age = int(input("Please enter your age: "))  # add variable name age and asked the user to input his/her age. The data type should be integer data type
years_from_now = "3"  # IndentationError - incorrect indentation
total_years = age + int(years_from_now)  # IndentationError - incorrect indentation and TypeError - unsupported operhand types for "int" and "str". Convert string "years_from_now" to an integer.

print(f"The total number of years: {total_years}")  # SyntaxError - missing the parentheses. To be able to print out to correct result we need to change the current print out to an f-string and add {total_year} 

# Variable to calculate the total amount of months from the total amount of years and printing the result
total = 27.5  # add variable name called total and assign the value of 27.5 to it
total_months = total * 12
print(f"In 3 years and 6 months, I'll be {total_months:.0f} months old")  # SyntaxError - missing the parentheses and TypeError: can only concatenate str (not "float") to str. Change print out to a f-sting. Remove "+ total_months +" and add {total_months:.0f} round it off to zero decimals.

#HINT, 330 months is the correct answer
