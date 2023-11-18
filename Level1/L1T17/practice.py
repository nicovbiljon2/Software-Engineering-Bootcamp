# using the open function

file = open("example.txt", "r+")  # perform operations on the open file
file.close

with open("example.txt", "r+") as file:
    lines = file.read()  # reads all the data in the file
    lines = file.read(10)  # reads the first 10 characters in the file
    lines = file.readline()  # reads a single line of data in the file
    lines = file.readlines()  # reads all the lines of data in the file
    for line in file:  # reads each line of data in the file
        print("The entire line is: " + line)
        print("The first character of this line is: " + line[0])

contents = ""  # store the contents

with open("exapmle.txt", "r+") as file:  # open the file
    for line in file:  # iterate through the lines
        contents = contents + line  # add the contents of each line
    print(contents)  # print the contents

# encoding method
file = open("example.txt", "r+", encoding="utf-8")
