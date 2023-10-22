# the if statement

num = 10 

if (num <12):
    print("the variable num is lower than 12")

print(num)

# example 1
age = 20
if age >= 18:
    print("You're over 18 and can come in.")

# this is an example program demostrating if statements.
name = input("Enter your name: \n")

if len(name) == 0:
    print("You didn't enter anything.")
if len(name) > 10:
    print("You've got a long name.")

print(name)

print()

# booleans in control statements
umbrella = "Leave me at home"
is_raining = False
if is_raining:
    umbrella = "Bring me with"

print(umbrella)

# example 1
is_sunny = True

if is_sunny:
    print("It is sunny today, don't forget the sunscreen!")

print()

# example 2
clean_car_red = True
clean_car_blue = True
clean_car_green = True
num_of_car = 0
busy = False

print("Welcome to the car wash")

red_check = input("Is the Red car Dirty? (Yes or No) ")  # Note input is case sensitive here
if red_check == "Yes":
    clean_car_red = False
blue_check = input("Is the Blue car Dirty? (Yes or No) ")  # Note input is case sensitive here
if blue_check == "Yes":
    clean_car_blue = False
green_check = input("Is the Green car Dirty? (Yes or No) ")  # Note input is case sensitive here 
if green_check == "Yes":
    clean_car_green = False

if clean_car_red == False:
    print("Red car really needs a cleaning")
    num_of_car += 1
if clean_car_blue == False:
    print("Blue car really needs a cleaning")
    num_of_car += 1
if clean_car_green == False:
    print("Green car really needs a cleaning")
    num_of_car += 1
    print(num_of_car)

if num_of_car == 3:
    busy = True

if busy == True:
    print("The car wash was packed today")
