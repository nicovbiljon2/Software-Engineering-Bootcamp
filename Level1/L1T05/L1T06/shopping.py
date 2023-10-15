# Write a program that asked the user to enter three product names and the price of each product. 
# Then calculate the total price of the three products
# The calculate the average price of the three products
# Print out the following sentence: "The Total of [product1], [product2], [product3] is Rxx,xx and the average price of the items is Rxx,xx."

# Print out a line that asked the user to enter three product names
# Create three variable names called "product1", "product2" and "product3"
# Store the user input into the three variable names "product1", "product2" and "product3"
# Print out another line asking the user to enter the price of each product
# Create another three variable names called "product_price1", "product_price2" and "product_price3". This should be a float data type
# Store the user input into the three variable names "product_price1", "product_price2" and "product_price3"
# Crate another variable name called "total_price"
# Calculate the total price by adding them all up and store the value into the variable name called "total_price"
# Create another variable name called "average_price"
# Calculate the average price by dividing the total_price by the number of products and store the value into the variable name "average_price"
# Print out the given sentence and insert the variable names into their respective places 

print("Please enter three product names: ")

product1 = input("Product name 1: ")
product2 = input("Product name 2: ")
product3 = input("Product name 3: ")

print("Please enter the products prices: ")

product_price1 = float(input("Product price 1: "))
product_price2 = float(input("Product price 2: "))
product_price3 = float(input("Product price 3: "))

sum = round(product_price1 + product_price2 + product_price3, 2)

average_price = round(sum / 3, 2)

print(f"The Total of {product1}, {product2}, {product3} is R{sum} and the average price of the itmes is R{average_price}.")

