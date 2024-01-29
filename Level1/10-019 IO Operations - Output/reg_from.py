# Write a program that allows a user to register students for an exam venue. First ask the user how many students
# are registering. Each time the the for loop runs the program should ask the user to enter the next student ID number. 
# Write each of the ID numbers to a text file called "reg_form.text". Include a dotted line after each student ID
# because this document will be used as an attendance register which the students will sign when they arrive at the
# exam venue.

reg_form = open("reg_form.txt", "w")  # peform operation to create and open file

amount_registering = int(input("How many students are you registering: "))  # request user input as an ingeter 

with open("reg_form.txt", "w") as reg_from:  # to create and open to perfom opreations on the file
    for id_number in range(amount_registering):  # the number of itteration that will happen in the loop is based on the user input
        id_number = int(input("Please enter student ID number: "))  # request student id numbers
        reg_form.write(str(id_number) + "\n...................." + "\n")  # write the user input to the text file called "reg_from"

