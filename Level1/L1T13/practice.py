# the for loop

for i in range(1, 10):
    print(i)

print()

# if and for loop statment
for i in range(1, 10):
    if i > 5:
        print(i)

print()

# loop with a break statement
num_list = [1, 2, 3, 4, 5]
found = False

num = int(input("Input a number from 1 to 10 and find out if it' in our list: "))

if num < 1 or num > 10:
    print("Number out of range")
else:
    for number in num_list:
        if num == number:
            found = True
            break
    print(f"List contains {num}: {found}")

print()

# nested loop
for x in range(1, 6):
    for y in range(1, 6):
        print(f"{x} * {y} = {x * y}")
    print("")

print()

# nested if statement
name = "B"
if name == "A":
    if name == "B":
        print("It isn't possible for this code to execute - how can the varialbe name be two things at once?")
else:
        print("Your name isn't A but I can't automatically assume from that it is B.")


# this program will print all the even numbers between 1 and 999
for num in range(1, 1000):
    if num % 2 == 0:
        print(num)



