#Task 1
#Calculate rectangle area:

#Take 2 console inputs (width and height) then calculate and print the area of the resulting rectangle. 

""" 
width = input("Please write the width:")
height = input("Please write the height:")
area = int(width) * int(height)
print(area) 
"""

#Task 2
#Greeting by name:

#Create a program, that takes your name as input and prints out the string 'Hello, {name}'

""" 
name = input("Please write your name:")
print(f"Hello, {name}") 
"""

#Task 3
#Print out strings and numbers:

#Create a program that takes 4 input parameters: first_name, last_name, age and town and 
#prints out the message 'You are {first_name} {last_name}, a {age}-years old person from {town}.'
""" 
first_name = input("Please write your first name:")
last_name = input("Please write your last name:")
age = int(input("Please write your age:"))
town = input("Please write the name of your hometown:")
print(f"You are {first_name} {last_name}, a {age}-years old person from {town}")
 """

#Task 4
#Yard greening:

#Create a program that calculates the sum needed to pay a company to landscape a yard. 
#The price per square meter is 7.61 lv. and there is a discount of 18% of the final price.
""" 
yard_size = float(input("Size of the yard:"))
price = yard_size * 7.61
discount = price * 0.18
print(f"The final price is: {price - discount} lv")
print(f"The discount is: {discount} lv.") 
"""


