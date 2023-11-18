string_list = ["John", "Mary", "Harry"]
# or
string_list1 = []  

# indexing a list
pet_list = ["cat", "dog", "hamster", "goldfish", "parrot"]
print(pet_list[0])
print(type(pet_list[0]))
print(type(pet_list))

print()
# slicing a list
num_list = [1, 4, 2, 7, 5, 9]
print(num_list[1:2])
print(num_list[2:4])

print()
# changing elements in a list
name_list = ["James", "Molly", "Chris", "Peter", "Kim"]
name_list[2] = "Tom"  # you can also using negative indexing for example [-3]
print(name_list)

print()
# adding elements to a list
new_list = [34, 35, 75, "Coffee", 98.8]
new_list.append("Tea")
print(new_list)

print()
# deleting elements from a list
char_list = ["p", "y", "t", "h", "o", "n"]
print(char_list)

char_list.pop()
print(char_list)

char_list.pop(0)
print(char_list)

char_list.remove("t")
print(char_list)

print()
# looping over a list
food_list = ["Pizza", "Burger", "Fries", "Pasta", "Salad"]
i = 0  # initialise i

while i < len(food_list):
    print(food_list[i])
    i += 1  # increment i, the loop counter

print()

for food in food_list:
    print(food)

print()
# checking if something is in a list
grocery_list = ["Bread", "Milk", "Butter", "Cheese", "Cereal"]

if "Apples" in grocery_list:
    print("The item Apples was found in the grocery_list")
else:
    print("The item Apples was not found in the grocery_list")

print("Are Apples included?", "Apples" in grocery_list)
# or
for item in grocery_list:
    if item == 'Apple':
        print("The item Apples was found in the grocery_list")

print()
# quickly populating lists
test_list1 = [7] * 5
print(test_list1)

test_list2 = ["Bob"] * 4
print(test_list2)

test_var = 6
test_list3 = [test_var] * 2
print(test_list3)

print()
# casting to a list
hello_string = "Hello world!"
hello_string = list(hello_string)
print(hello_string)

num_till_10 = list(range(0, 11))
print(num_till_10)

num_till_5 = list(range(0, 6))
print(num_till_5)
