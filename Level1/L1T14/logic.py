# This program asked the user to enter some numbers and then calculate the average of the numbers entered by the user. 
# If they enter zero the program will exit and print out the result

numbers = 0

while True:
    user_input = float(input("Please enter some numbers (enter 0 to exit): "))
    numbers += user_input
    
    if user_input == 0:
       print(f"The total number entered is {numbers}.")
       break
         
average_number = numbers / len(str(numbers)) 
print(f"The average of all the numbers entered is {average_number:.2f}.")
