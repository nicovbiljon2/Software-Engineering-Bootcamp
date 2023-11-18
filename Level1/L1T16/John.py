# Write a program called John.py that takes the user's inputs as a string.
# The program should not be affected by capital letters inputted by the user.
# While the string is not "John" the program should keep on asking the user to enter,
# his/her name until the user enters the name "John". 
# The program should then stop running and print out a complete list of all the incorrect names entered.

incorrect_user_name = []  # I create an empty list to store all the incorrect names inputted by the user

while True:
    user_name = input("Please enter your name: ").capitalize()  # I used the capitalize() method to eliminate the case sensitivity 
    if user_name == "John":
        break
    incorrect_user_name.append(user_name)   
           
print(f"List of incorrect names entered: {incorrect_user_name}")
     
