# Write a program that reads the data from the text file provided (DOB.txt) and prints out in two
# different sections in the format displayed below:

# Name
# Orville Wright
# Rogelio Holloway
# Marjorie Figueroa
# …etc

# Birthdate
# 21 July 1988
# 13 September 1988
# 9 October 1988
# …etc

# perform a operation to open the text file
file = open("DOB.txt", "r")

names = []  # empty list which will store all the names from the "DOB.txt" file
birthdates = []  # empty list which will store all the birthdayes from the "DOB.txt" file
n = ""
b = ""
line_count = 0  # to count the number of lines in the names text file 
line_count1 = 0 # to count the number of lines in the birthdates ext file

with open("DOB.txt", "r") as file:  # file opened to perfom opreations on the file
    for line in file:  # to iterate throught the lines in the open file
        line = line.split()  # split the lines into  5 pieces (name, surname, date, month, year)
        names.append(line[0] + " " + line[1])  # the first 2 pieces will be added to the lits called names
        birthdates.append(line[2] + " "+line[3] + " " +line[4])  # the last 3 pieces will be added to the list called birthdates 

    print("Name")
    for name in names: 
        line_count += 1
        if line_count in range(0, 4):  # to print a specific number of lines of the names 
            print(f"{str(n)}{name}")  # print each name in the list on a separate line
    print("...etc")   
    
    print()

    print("Birthday")        
    for birthdate in birthdates:
        line_count1 += 1
        if line_count1 in range(0, 4):  # to print a specific number of lines of the birthdays
            print(f"{str(b)}{birthdate}")  # to print each birthdate in the list on a separate line
    print("...etc")

file.close()
