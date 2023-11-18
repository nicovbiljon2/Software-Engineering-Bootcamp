string = "Hello"

print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])

print()

original_string = "Hello world!"
new_string = original_string[0:5]

print(new_string)

print()
# recap on slicing a string

fizz = "Hello world!"
fizz = string[0:5]
print(fizz)

fact1 = "The original name of Windows was Interface Manager."
fact1 = fact1.upper()
print(fact1)
fact1 = fact1.lower()
print(fact1)

print()

sentence = "ThisHELLOisHELLOrandomHELLOtextHELLOweHELLOareHELLOgoingHELLOtoHELLOsplitHELLOapart"
split_sentence = sentence.split("HELLO")
print(split_sentence)

print()

fact2 = "          The$first$electronic$computer$ENIAC$weighed$more$than$27$tons.          "
fact2 = fact2.replace("$", "WOW!")
print(fact2)
fact2 = fact2.strip()
print(fact2)
fact2 = fact2.split("WOW!")
print(fact2)

print()

string_list = ["I", "like", "to", "join", "lists", "to", "make", "strings"]
list_joined = " ".join(string_list)
print(list_joined)

print()

people = "Person 1 \nPerson 2"
print(people)

wage = "Person 1 \t 123.22"
print(wage)

print()

sentence1 = "\"The escape character (\\) is a character which invokes an alternative interpretation of subsequent characters\
 in a character sequence.\""
print(sentence1)

print()
# escape character
print("Hello \n\"bob\"")
print("The escape sequence \\n creates a new line in a print statement")

print()
# string building
name = "Peter"
print("Hello, {}!".format(name))
# or the f-string
name1 = "Hendrik"
print(f"Hello, {name1}!")

# string building with a for loop
number_builder = ""
i = 0

while i <= 50:
    if i % 2 == 0:
        number_builder += str(i) + " "
    i += 1

print(number_builder)

# using the .join() method
number_builder1 = []  # creating a empty list, the variable has to be a list rather than a string
i = 0

while i <= 52:
    if i % 2 != 0:
        number_builder1.append(str(i))
    i += 1

print(" ".join(number_builder1))

print()

sentence2 = "Hello World"
final_sentence2 = ""  # empty string 

for i in range(len(sentence2)):
    if i % 2 == 1:
        final_sentence2 += sentence2[i].upper()  # concatenate with sentence index by i
    else:
        final_sentence2 += sentence2[i].lower()

print(final_sentence2)

print()

fruit = ["apples", "bananas", "mango", "orange", "cherries", "strawberries"]

print("@".join(fruit))
