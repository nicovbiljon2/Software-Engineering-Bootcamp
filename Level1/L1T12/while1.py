# calculate the sum and average of n integer numbers exercise:

count = 0
total_sum = 0.0
number = 1

while number != 0:
    number = int(input("Please enter some number. Enter -1 to exit: "))
    total_sum += number
    count += 1

if count == 0:
    print("Enter some numbers:")
else:
    print(f"The average of all the numbers entered is", total_sum / (count - 1), total_sum)




