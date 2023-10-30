# Design a program that determines the award a person competing in a triathlon will receive. The program should read
# in the times (minutes) for all three events namely swimming, cycling and running. 
# The award is based on the total time of all three events. The qualifying criteria is as follows:
# 0 to 100 minutes Provisional Colours, 101 to 105 Provisional Half Colours, 106 to 110 Provisional Colours
# and 111+ minutes No award.

# Create variable names called "swimming", "cycling" and "running"
# Request user inputs and store it in variable names called "swimming", "cycling" and "running". 
# Convert the input data to an integer data type
# Create a variable name called "total_time"
# Calculate the total_time by adding up all the three variable names called "swimming", "cycling" and "running"
# if the user "total_time" is less or equal than 100
# 	print out "Your total qualifying time is {total_time}, and you qualify for a Provincial Colours"
# elif the user "total_time" is grater than 100 and less or equal than 105
# 	print out "Your total qualifying time is {total_time}, and you qualify for a Provincial Half Colours"
# elif the user "total_time" is greater than 105 and less or equal to 110
# 	print out "Your total qualifying time is {total_time}, and you qualify for a Provincial Scroll"
# else:
# 	"Your total qualifying time is {total_time}, and you do not qualify for an Award"

swimming = int(input("Please enter your total swimming time in minutes: "))
cycling = int(input("Please enter your total cycling time in minutes: "))
running = int(input("Please enter your total running time in minutes: "))

total_time = swimming + cycling + running

if total_time <= 100:
    print(f"Your total qualifying time is {total_time}, and you qualify for an Provincial Colours.")
elif total_time > 100 and total_time <= 105:
    print(f"Your total qualifying time is {total_time}, and you qualify for an Provincial Half Colours.")
elif total_time > 105 and total_time <= 110:
    print(f"Your total qualifying time is {total_time}, and you qualify for an Provincial Scroll.")
else:
    print(f"Your total qualifying time is {total_time}, and you do not qualify for an Award.")
  
