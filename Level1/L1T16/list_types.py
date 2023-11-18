# Create a list called "friends_name" and write the correct syntax to store 3 of your friends full names
# Write a statement that prints out the first and last name of the list and lastly the length of the list
# Create a another list called "friends_ages" to store your friends age in a corresponding manner,
# i.e., first entry of the age is the for the first friend name in the other list.

friends_name = []

friends_name.append("Wessel van Niekerk") 
friends_name.append("Milton Kukard")
friends_name.append("Dean Higgins")

print(friends_name)
print(friends_name[0])
print(friends_name[2])
print(len(friends_name))

print()

friends_ages = []

for age in [60, 54, 46]:
    friends_ages.append(age)

print(friends_ages)

 
