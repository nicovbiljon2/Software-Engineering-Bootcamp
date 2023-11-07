# Write a program to output the star pattern show below, using an if-else statement in combination with a single for loop.
# **
# *
# ***
# ****
# *****
# ****
# ***
# **
# *

row_count = 10

for i in range(1, row_count):
    if i <= 5:
        print("*" * i)
    else:
        print("*" * (10 - i))
