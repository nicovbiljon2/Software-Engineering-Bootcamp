# the elif statements

num = 10

if num > 12:
    print("the variable num is greater than 12")
elif num > 10:
    print("the variable num is greater than 10")
elif num < 10:
    print("the variable num is less than 10")
else:
    print("the variable num is 10")

# example 2
robot = input("Enter the colour of the robot light: ")

if (robot == "yellow"):
    print("You must slow down.")
elif (robot == "green"):
    print("You can drive")
elif (robot == "red"):
    print("You must stop")
else:
    print("The colour of the robot light, which you have entered, is incorrect.")

# example 3
letter = input("Enter A, B or C: ")

if (letter == "A"):
    print("A is for Apple")
elif (letter == "B"):
    print("B is for Bananna")
elif (letter == "C"):
    print("C is for Carrot")
else:
    print("The letter you have entered is incorrect.")
