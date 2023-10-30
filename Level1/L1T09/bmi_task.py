# Write a program that calculates a person's BMI

# Create a variable name called "weight"
# Request user input and store it into variable name called "weight". Convert the data type to an integer data type
# Create a variable name called "height"
# Request user input and store it into variable name called "height". Convert the data type to an float data type
# Create a variable name called "BMI" 
# Use the following formula to calculate the user's "BMI"
# BMI = (weight in kg) / (height in m) * (height in m). 
# Note the data type for weight should be an integer and for height an float data type.
# Round the answer to two decimals

# if the use's "BMI" is greater than or equal to 30
# 	print out " Your BMI is {BMi}, and you are obese."
# elif the user's "BMI" is greater than or equal to 25
# 	print out "Your BMI is {BMi}, and you are overweight."
# elif the user's "BMI" is greater than or equal to 18.5
# 	print out "Your BMI is {BMi}, and you are normal."
# else
# 	print out "Your BMI is {BMi}, and you are underweight."

weight = int(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in m: "))

BMI = round(weight / (height * height), 2)

if BMI >= 30:
    print(f"Your BMI is {BMI}, and you are obese.")
elif BMI > 25:
    print(f"Your BMI is {BMI}, and you are overweight.")
elif BMI > 18.5:
    print(f"Your BMI is {BMI}, and you are normal.")
else:
    print(f"Your BMI is {BMI}, and you are underweight.")

