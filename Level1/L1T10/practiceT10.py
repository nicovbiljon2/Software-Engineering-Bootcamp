# comparison operators
# comparing strings:
my_name = "Tom"
if my_name == "Tom":
    print("I was looking for you")

# comparting numbers:
num1 = 10
num2 = 20

if num1 >= num2:
    print("It's not possible that 10 is bigger than or equal to 20.")
elif num1 <= num2:
    print("10 is less than or equal to 20.")
elif num1 != num2:
    (print("""This is also true since 10 isn't equal to 20, but the elif
            statement before comes first and is true so Python will excute that!"""))
elif num1 == num2:
    print("Will never execute this print statement...")

# logical operators
# example of an and operation
team1_score = 3
team2_score = 2
game = "Over"

if (team1_score > team2_score) and (game == "Over"):
    print("Congratulations you have won the match!")

# example of on or operation
speed = int(input("How many kilometers per hour are you travelling at? "))
belt = input("Are you wearing a safety belt? ")

if (speed > 80) or (belt != "Yes"):
    print("Sorry Sir, but I have to give you a traffic fine.")

# Example 1

my_name1 = "Piet"
my_favourite_colour = "blue"

if my_name1 == "Piet":
    print("Your name is Piet and your favourite colour is blue.")
else:
    print("Your name is not Piet or your favourite colour isn't blue.")

# Example 2
# or operator
item = "chair"

if item == "dog" or len(item) == 5:
    print("Either item is a dog, or the lenght of your item is 5.")
# and operator
elif item == "chair" and len(item) == 5:             
       print("Your item is both a chair and len of item is 5.")

# Example 3
has_traffic_fines = False

if not has_traffic_fines:
    print("You are a good driver.")

