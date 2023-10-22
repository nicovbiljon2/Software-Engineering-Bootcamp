# if statement
num = 10

if num < 12:
    print("the variable num is lower than 12")

# else statement
current_time = 12

if current_time < 11:
    print("Time for a short jog - let's go!")
else:
    print("It's after 11 - it's lunch time.")
    
hour = 18

if hour < 18:
    greeting = "Good morning"
else:
    greeting = "Good evening"

print(greeting)

# Example 1
grade = 66

if grade >= 80:
    print("Congratulations you have an A")
else:
    print("You do not have an A")

# Example 2
if 9 == "9":  # comparing an ingeter and a sting 
    print("Types don't matter")
else:
    print("Types do matter")

if 9 == int("9"):
    print("Successful casting")
else:
    print("I didn't need to cast that!")


# demostrating if statements

name = input("Enter your name: \n")

if len(name) == 0:
    print("You didn't enter anything.")
else:
    if len(name) > 10:
        print("You've got a long name.")

age = int(input("Thanks for entering your name. Please enter your age: \n"))

print(name)
print(age)


