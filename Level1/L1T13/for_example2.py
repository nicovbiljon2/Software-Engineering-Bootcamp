# demostrating for loops
# it asks for the user to input a number to the given_number variable
# if the number is even, a for loop prints out an increasing * pattern
# if the number is odd, a for loop prints out a decreasing * pattern

given_number = int(input("Enter a number: \n"))

if given_number % 2 == 0:
    stars = "*"
    for i in range(0, 10):
        print(stars)
        stars = stars + "*"
    
elif given_number % 2 != 0:
    stars = "**********"
    for i in range(0, 10):
        index = 10 - i  # i goes from 0 to 10 in this loop
        print(stars[0:index])  # index gets smaller as the loop goes on i.e from [0:10] to [0:1] 
                               # i.e fewerof the 10 original star will be printed out
