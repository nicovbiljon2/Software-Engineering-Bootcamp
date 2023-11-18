
# Write a program that reads in a string and make each alternate character an upper case and each
# other alternate character a lower case character.
# Now, try starting with the same string but making each alternative word lower and upper case.

# part 1 characters in upper and lower case:
sentence = "I am passionate about learing to code"
new_sentence = ""  # create a empty string

for i in range(len(sentence)):
    if i % 2 == 0:
        new_sentence += sentence[i].upper()
    else:
        new_sentence += sentence[i].lower()

print(new_sentence)

print()

# part 2 - words in upper and lower case:
sentence1 = " I am passionate about learning to code"
split_sentence1 = sentence1.split()  # split the sentence into words
new_sentence1 = ""  

for i in range(len(split_sentence1)):
    if i % 2 == 0:
        new_sentence1 = new_sentence1 + " " + split_sentence1[i].lower() 
    else:
        new_sentence1 = new_sentence1 + " " + split_sentence1[i].upper() 

final_sentences1 = "".join(new_sentence1)  # joining the individual characters together

print(final_sentences1)

