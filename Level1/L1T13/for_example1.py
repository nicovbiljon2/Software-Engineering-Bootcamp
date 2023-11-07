# the user inputs a number
# the program then outputs all the EVEN numbers from 0 to that number, using a for loop and if statement

print("*Printing even numbers in a range*")
range_num = int(input("Enter the upper bound of the range (nax number you'd like to go up to): \n"))

for i in range(0, range_num):  # we define a for loop that runs from 0 to the entered number.i is the current number that the loop is on
          if i % 2 == 0:  # this checks if the number of the loop is EVEN (divide it by 2 you get 0 remained)
               print(i)