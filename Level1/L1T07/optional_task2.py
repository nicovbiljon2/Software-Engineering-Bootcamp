# Write a program that will help the user to decide what to wear. To determine this we should ask the user some yes and no questions,
# based on the temperature of 20 degree, if it is sunny or not and if it is weekend or a weekday. 

# Create variable names called "temperature", "weekend" and "sunny"
# Request user input by answering some questions "yes" or "no". 
# "yes" = "True" and "no" = "False"
# if temperature equals "yes" 
#	 print out "You should wear a short-sleeved shirt when the temperature is higher than 20 degrees."
# else temperature equals "no"
#	 print out "You should wear a long-sleeved shirt when the temperature is lower than 20 degrees."
# if weekend equals "yes"
#	 print out "You should wear shorts when it is weekend."
# else weekend equals "no"
#	 print out "You should wear jeans when it is a weekday."
# if sunny equals "yes"
#	 print out "You should wear a cap when it is sunny outside."
# else sunny equals "no"
#	 print out "You should wear a raincoat when it is not sunny outside."

temperature = input("Is the temperature higher than 20 degrees(yes or no): ")

if temperature == "yes":
    print("You should wear a short-sleeved shirt when the temperature is higher than 20 degrees.")
else:
    print("You should wear a long-sleeved shirt when the temperature is lower than 20 degrees.")

weekend = input("Is it weekend(yes or no): ")

if weekend == "yes":
    print("You should wear shorts when it is weekend.")
else:
    print("You should wear jeans when it is a weekday.")

sunny = input("Is it sunny outstide(yes or no): ")

if sunny == "yes":
    print("You should wear a cap when it is sunny outside.")
else:
    print("You should wear a raincoat when it is not sunny outside.")
    