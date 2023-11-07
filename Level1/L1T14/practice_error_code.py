# this is an example program to demonstrate error
# there are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
 
name = "Tim"
#    surname = " Jones"
surname = "Jones"  
age = 21
 
#full_message = name + surname +  is  + age + " years old"
full_message = name + " " + surname + " " +  "is" +  " " + str(age) + " " + "years old" 
                                                          
print (full_message)  

# line 5 - syntax error - incorrect indentation. "surname should be in line with "name" and "age".
# line 8 - syntax error - "is" is under the wrong syntax, needs to be within " ". 
# line 8 - runtime error - "age" is a ingeter data type. Can't concatenate a string to an ingeter.  
# To resolve this error convert "age" to a string data type.
# line 10 - syntax error - full_ message does not have appropriate spacing require: + " " +.

# example 2
# numbers = [1, 2, 3, 4, 5]
# sum = 0

# for i in range(10):
#     sum += numbers[i]

# print("The sum of the numbers is: ", sum)

# This code intends to calculate the sum of the numbers in the numbers list. 
# The problem, however, is that the logic in the loop condition is incorrect as it will attempt to access the numbers 
# list using indices 5-9, which do not exist.
# The solution is to change the loop condition to loop over the indices of the numbers list, rather than a fixed range:
#       for i in range(len(numbers)):
#           sum += numbers[i]

# example 3
# grade_score = 80

# if grade_score > 50:
#     print("Grade: C")
# elif grade_score > 75:
#     print("Grade: B")
# elif grade_score > 85:
#     print("Grade: A")
# else:
#     print("Grade: F")

# The logical error in the above code is the order of the if statements. 
# Since the if statements are evaluated in order, the current code will first check if 'grade_score' 
# is greater than 50, which is True since 'grade_score' is 80, so it will print "Grade: C" and skip the remaining statements. 
# The subsequent elif statements will not be evaluated, so "Grade: C" will always be printed.
# To fix this issue, the order of the if and elif statements should be reversed, so that the most restrictive conditions
# are checked first, like this:
#   if grade_score > 85:
#       print("Grade: A")
#   elif grade_score > 75:
#       print("Grade: B")
#   elif grade_score > 50:
#       print("Grade: C")
#   else:
#       print("Grade: F")
# Now, the most restrictive condition is checked first, and if it is not met, then the next condition is checked, and so on. 
# This will correctly print "Grade: B" for a grade_score of 80, which falls between 75 and 85.

# example 4
# area_trapezoid = 3 + 5 * 6 / 2
# print(area_trapezoid)

# The code above should calculate the area of a Trapezoid with parallel sides of length 3 and 5, and a height of 6.
# The area of this trapezoid should be 24, but when you run this program, you see that this is not the case. 
# The error arises due to the incorrect order of operations. The solution here is to add the missing brackets around 3 + 5
# The statement should be:
#       area_trapezoid = (3 + 5) * 6 / 2
