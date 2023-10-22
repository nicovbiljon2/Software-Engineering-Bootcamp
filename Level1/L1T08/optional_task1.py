# Design a program for a department store to calculate the monthly wage for two different types of employees 
# (salesperson and manager).
# The salesperson earns 8% commission on their monthly gross sales and a fixed sales of R2000.00. 
# The manager earns an hourly rate of R40.00.

# Create a variable name called "fixed_salary" and assign a value of 2000 to this variable
# Create a variable name called "commission" and assign a value of 8 to this variable
# Create a variable name called "hourly_rate" and assign a value of 40 to this variable
# Create a variable name called "employee" 
# Request user input to confirm their position (salesperson or manager)

# if "employee" equal "salesperson"
# 	create a variable name called "gross_sales" and request user input for their monthly gross sales,
#   and convert the date type to a float data type
# 	if gross_sales
# 		create a variable name called "sales person" to calculate the monthly income by dividing the "commission" by hundred,
# 		and then multiply the answer by the "gross_sales" amount. Then add the "fixed_salary" amount to the answer,
#       and convert data type to a float data type
# 		print out "Your monthly wage is R{salesperson:.2F} and round the answer off to two decimals
# else
# 	create a variable name called "hours_worked" and request use input to enter their number of hours worked for the month,
#   and convert data type to a float data type
# 	if hour_worked
# 		create a variable name called "manager" to calculate the monthly wage by multiplying the "hour_rate" by "hours_worked",
#       and convert data type to a float data type
# 		print out "Your monthly wage is R{salesperson:.2F} and round the answer off to two decimals

fixed_salary = 2000  # This is the fixed salary amount for the sales person
commission = 8  # this is the commission percentage for the sales person
hourly_rate = 40  # this is the hourly rate for the sales manager

employee = input("Please enter your positon(salesperson or manager): ")

if employee == "salesperson":
    gross_sales = float(input("Please enter your monthly gross sales: "))
    if gross_sales:
        salesperson = float((commission / 100) * gross_sales) + fixed_salary 
        print(f"Your monthly wage is R{salesperson:.2f}")
else:
    hours_worked = float(input("Please enter the number of hours worked for the month: "))
    if hours_worked:
        manager = float(hourly_rate * hours_worked)
        print(f"Your monthly wage is R{manager:.2f}")









    
