# sum1 = 0
# i = 2

# while sum1 <= 250:
#     sum1 += 1
#     i += 2
#     print(sum1)

# i = 0
# while i < 10:
#     i += 1
#     print(i)

# print()

# n = 0
# while n < 20:
#     n += 2
#     print(n)

# my_number = 0

# while my_number < 100:
#     my_number += 1
#     if my_number == 24:
#         break
#     print(my_number)

# print()

# my_number1 = 0

# while my_number1 < 50:
#     my_number1 += 1
#     if my_number1 > 24:  
#         continue
#     print(my_number1)  # will stop printing the numbers when it reaches the value 24.

# a = 0

# while a < 10:
#     print(a)
#     a += 1
 
# sum1 = 0
# i = 0

# while sum1 <= 250:
#     sum1 += i
#     i += 2
#     print(sum1)

start = 5

while start % 2 != 0:
    print(start)
    start = start + 1
    
print()

number = int(input("Enter a number less than 100: "))

while number > 100:
    print("Please try again")
    number = int(input("Enter a number less than 100: "))

if number % 2 == 0:
    print(number * 2)
else:
    print(number * 3)

print()

import random 

num = random.randint(1, 50)  # use the randint (i.e random integer) function from random library to get a random 
                             # integer between 1 an 50
num_guess = int(input("Guess a number from 1 to 50: "))

while num_guess != num:
    if num_guess < num:
        num_guess = int(input("Too small! Guess another number from 1 to 50: "))
    else:
        num_guess = int(input("Too big! Guess another number from 1 to 50: "))

print("You guessed correctly!")
