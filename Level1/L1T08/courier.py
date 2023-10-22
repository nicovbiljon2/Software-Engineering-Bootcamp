# Design a program for a courier company that calculates the cost of sending parcels.
# The cost needs to factor in the the following user inputs:
# Distance, Freight, Insurance, Gift, Priority and Parcel

# Create a variable name called "distance"
# Request user input and store it into the variable name called "distance" as an integer data type

# Create a variable name called "freight"
# Create a variable name called "air_freight" and assign a value of 0.36 to this variable
# Create a variable name called "land_freight" and assign a value of 0.25 to this variable
# Request user input to select the type of transport required (air or land)
# if "freight" equals "air_freight"
# 	calculate the "freight" by multiplying the "air_freight" value by the "distance" value
# 	this is to get the total freight cost and convert the data type to a float data type
# else
# 	calculate the "freight" by multiplying the "land_freight" value by the "distance" value
# 	this is to get the total freight cost and convert the data type to a float data type

# Create a variable name called "insurance"
# Create a variable name called "full_insurance" and assign a value of 50.00 to this variable
# Create a variable name called "limited_insurance" and assign a value of 25.00 to this variable
# Request user input to select the type of insurance required (full or limited)
# if "insurance" equals "full_insurance"
# 	assign "full_insurance" value to this variable name "insurance",
#   and covert the data type to a float data type
# else
# 	assign "limited_insurance" value to this variable name "insurance",
#   and convert the data type to a float data type

# Create a variable name called "gift"
# Create a variable name called "gift_cover" and assign a value of 15.00 to this variable
# Create a variable name called "no_gift" and assign a value of 0 to this variable
# Request user input if they require gift cover (yes or no)
# if "gift" equals "gift_cover"
# 	assign "gift_cover" value to this variable name "gift" and convert the data type to a float data type 
# else
# 	assign "no_gift" value to this variable name "gift" and convert the data type to a float data type
	
# Create a variable name called "priority"
# Create a variable name called "priority_del" and assign a value of 100 to this variable
# Create a variable name called "standard_del" and assign a value of 20 to this variable 
# Request user input to select the type of delivery required (priority or standard)
# if "priority" equals "priority_del"
# 	assign "priority_del" value to this variable name "priority" and convert the data type to a float data type 
# else
# 	assign "standard_del" value to this variable name "priority" and convert the data type to a float data type

# Create a variable name called "parcel"
# Create a variable name called "postage_sleeve" and assign a value of 100 to this variable
# Create a variable name called "postage_box" and assign a value of 150 to this variable
# Request user input to select the type of postage parcel required (sleeve or box)
# if "parcel" equals "sleeve"
# 	assign "postage_sleeve" value to this variable "parcel" and convert the data type to a float data type
# else
# 	assign "postage_box" value to this variable "parcel" and convert the data type to a float data type

# Create a variable name called "total_cost"
# Calculate the "total_cost" by adding up all the variable names,
# "freight" plus "insurance" plus "gift" plus "priority" plus "parcel". Round the total to two decimals.

# Print out "Your total cost for sending this parcel is {total_cost:.2f}."

distance = int(input("Please enter the total distance of the delivery: "))

freight = input("Please select the type of freight required(air or land): ")
air_freight = 0.36  # this is the rate for air freight per kilometer
land_freight = 0.25  # this is the rate for land freight per kilometer

if freight == "air":
    freight = float(air_freight * distance)
else:
    freight = float(land_freight * distance)

insurance = input("Please select the type of insurance required(full or limited): ")
full_insurance = 50  # this is the price for full insurance 
limited_insurance = 25  # this is the price for limited insurance 

if insurance == "full":
    insurance = float(full_insurance)
else:
    insurance = float(limited_insurance)

gift = input("Do you require gift cover(yes or no): ")
gift_cover = 15  # this is the price for gift cover
no_gift_cover = 0  # this is the price for no gift cover

if gift == "yes":
    gift = float(gift_cover)
else:
    gift = float(no_gift_cover)

priority = input("Please select the type of priority required(priority or standard): ")
priority_del = 100  # this is the price for priority delivery
standard_del = 20  # this is the price for standard delivery 

if priority == "priority":
    priority = float(priority_del)
else:
    priority = float(standard_del)

parcel = input("Please select the type of postage parcel required(sleeve or box): ")
postage_sleeve = 100  # this is the base fee for the postage sleeve
postage_box = 150  # this is the base fee for the postage box

if parcel == "sleeve":
    parcel = float(postage_sleeve)
else:
    parcel = float(postage_box)

total_cost = round(freight + insurance + gift + priority + parcel, 2)

print(f"Your total cost for sending this parcel is R{total_cost:.2f}.")






