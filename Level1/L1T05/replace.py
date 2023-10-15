# Write a program that stores this sentence “The!quick!brown!fox!jumps!over!the!lazy!dog.”.
# Reprint this sentence without the exclamation marks.
# Reprint the same sentence with all the word capitalized.
# Reprint the same sentence in reverse.

# Create a variable name called "sentence"
# Store the given sentence into the variable name called "sentence"
# Create a new variable name called "new_sentence"
# Store the variable name "sentence" into the new variable name called "new_sentence"
# Use the replace method to remove the exclamation marks and replace them with whitespaces
# Print out the variable name "new_sentence"
# Print out the variable name "new_sentence" with all the characters capitalized using the upper method
# Print out the variable name "new_sentence" in reverse using the slicing method

sentence = '"The!quick!brown!fox!jumps!over!the!lazy!dog."'
new_sentence = sentence.replace("!", " ")

print(new_sentence)

print(new_sentence.upper())
print(new_sentence[::-1])
