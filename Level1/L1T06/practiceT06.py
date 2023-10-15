import math

# class_list = 25 # integer
# interest_rate = 12.23 # float

# casting between numbers
num1 = 12
num2 = 99.99

print(float(num1))
print(int(num2))

# arithmetic operations (calculations)
sum = 2 + 4
print(sum)

cents = 0.25 + 4.33
print(cents)

print()

# mathematical functions
number = 66.6564544
print(round(number, 2))

numbers_list = [6, 4, 66, 35, 1]
print(min(numbers_list))

numbers_list = [6, 4, 66, 35, 1]
print(max(numbers_list))

# numbers_list = [6, 4, 66, 35, 1] - TypeError: 'int' object is not callable when you run this code. It outputs 112 when I run it in Thonny
# print(sum(numbers_list))

print()

# mathematical functions available through the math module. To use these functions add this line of code import math
print(math.floor(30.3333))  # rounds a number down
print(math.ceil(30.3333))  # rounds a number up
print(math.trunc(30.33333))  # cuts off the decimal part
print(math.sqrt(4))  # finds the square root of a number
print(math.pi)  # retuns the value of pi
