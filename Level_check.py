# Task 1: Number Manipulation
# Write a Python program to calculate the factorial of a given number
""" 
number = int(input("I want the factorial of:"))
if number < 0:
   print("Not possible")
elif number == 0:
   print(0)
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i

    print(factorial)
 """

# Task 2: String Formatting
# Description : Write a Python program to accept a first name, last name, and a sum of
# money (as a float). Print a formatted string in the following form: "Hello [first_name]
# [last_name], you have $[amount] in your account."

""" first_name = input("Please write your first name:")
last_name = input("Please write your last name:")
sum = float(input("Please write your sum:"))

print(f"Hello {first_name} {last_name}, you have ${sum} in your account.") """

#Task 3: List Operations
#Description : Create a list of even numbers from 1 to 20. Then, remove all numbers
#divisible by 5.
""" 
my_list = []
for i in range(1, 21):
    if i % 2 == 0:
        my_list.append(i)

print(my_list)

for x in my_list:
    if x % 5 == 0:
         my_list.remove(x)

print(my_list) """

#Task 4: Student Average Grade
#Description : Create a dictionary to store the grades of students in a class (keys:
#student names, values: grades). Write a function to calculate the average grade of the
#class.

""" my_dict = {}
number = int(input("Please write the number of students in the class:"))
for i in range(0, number):
    student_name = input("Please write the student's name:")
    grade = float(input("Please write the student's grade:"))
    my_dict[student_name] = grade

sum = 0
for k in my_dict.values():
    sum += k
print(sum/number) """

#Task 5: File Processing
#Description : Write a Python function to read a text file ("text.txt") and count how
#many times each word appears in the file, afterwards print first by occurance times and
#then in alphabetic order of letters for words that have the same number of occurances.


#Task 6: Function with Parameters and Return
#Description : Define a function calculate_area that accepts the type of shape ("circle",
#"rectangle"), and the necessary dimensions (e.g., radius for a circle, length and width for a
#rectangle). It should calculate the area and return it.

""" shape = input("Please write the shape:")
if shape == "rectangle":
        dimensions = []
        for i in range(0, 2):
            dimension = float(input("Please write the lenghth and then the width:"))
            dimensions.append(dimension)
if shape == "circle":
     dimensions = float(input("Please write the radius:"))

def calculate_area(shape, dimensions):
    if shape == "rectangle":
        area = float(dimensions[0]) * float(dimensions[1])
    elif shape == "circle": 
        area = 3.14 * dimensions * dimensions
    print(area)
         
calculate_area(shape, dimensions) """


#Task 7: Student Management System
#Description : Write a program to build a simple Student Management System using
#Python. You will need 2 classes: Student(first_name:str, last_name:str, student_id:int,
#age:str) and a class to contain all students - StudentManagement, which needs to have a
#way to keep record of all students and has the following methods:


#Task 8: Correct email matcher
#Description : Define the function phone_matcher, which takes a string as it's
#parameter, and check if the string is a valid phone number. The valid formats are +000
#000000000 (can be any digit) OR 0000000000. If there is an invalid character or the phone
#is invalid, print "Invalid phone number!"

""" phone = input("Please write your phone:")
#+000000000000
def phone_matcher(phone):
    if len(phone) == 10:
        print("Valid phone number!")
    elif len(phone) == 14:
        if phone[0] == "+" and phone[4] == " ":
            print("Valid phone number!")
        else:  
            print("Invalid phone number!")
    else:  
        print("Invalid phone number!")
phone_matcher(phone) """ 
# Will not work with +359 887605061
# Fixed ^


#Task 9: Old phone
#Description : Define a function named old_phone, that takes a string that contains
#either 1, 2 or 3 of the same digits ("1", "22", "555") and convert it to how our old flip-phones
#worked. 1 is A, 11 is B, 111 is C, 2 is D and so on.

""" number = input("Number:") 
def old_phone(number):
    flag = True
    length = len(number)
    if length > 3:
       print("Incorrect string!")
    else:
        for i in range(0, length - 1):
            if number[i] != number[i+1] or number[i] == "0":
                print("Incorrect string!")
                flag = False
                return 0
        if flag == True:
            alpha_num = 64 + (int(number[0]) - 1) * 3 + length
            print(chr(alpha_num))    

old_phone(number) """

# When passed the example output, it returns errors, also the break only breaks the loop, but does not return from the function, so even in an incorrect scenario, it will try to return a string.
# Fixed ^
#Task 10: Fix test file
#Description : Define a function named xml_automation, that reads the testsuite.xml file in this folder and adds to the description tag the string "(Automated)"
#(example: "Tests basic subtraction functionality" becomes "
#(Automated) Tests basic subtraction functionality" ), but only for the tests
#with tag subclass Recovery , and then writes it to a new file named test-automated.xml.
