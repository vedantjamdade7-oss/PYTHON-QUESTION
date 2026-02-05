# Q-1. Leap year: Write a simple program to determine if a given year is a leap year using user input

# Note:
# Leap year occurs once every four years.
# 4 divisible & 100 not divisible
# 400 divisible

# user input
year = int(input("Enter a year :")) 

# checking leap year
if  (year % 4 == 0 and year % 100  != 0) or (year % 400 == 0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

# Q-2. Write a program, Who are Eligible for vote

# Eligible of vote

age = int(input("Enter a year :"))
if age >= 19:
    print(f"{age} yes, you are Eligible for vote")
else:
    print(f"{age} NO, you are not Eligible for vote")


# Q-3. Login Authentication using condition statement. Assume you have a predefined username and password

# note: Write a program that prompts the user to enter a username and password and checks wether they match. Provide appropriate message for the following cases:
#Both username and password are correct
# Username is correct but password is incorrect
# Username is incorrect.


# predefind username and password
predefined_username = 'vedant'
predefined_password = 'vedu69'

# prompts the user to enter a username and password
username = input("Enter your username :")
password = input("Enter your password :")

# username and password match
if username == predefined_username:
   if password == predefined_password:
    print("welcome! Login was successful.")
   else:
    print("Incorrect password!")
else:
    print("Invalid username!")

# Q-4. Admission Eligibility: A university has the following eligibility criteria for admission:
# note: Mathematics, Physics and Chemistry
# Total marks in all three sub>=180 OR total marks in mathematics and Physics>=140.

# Admission Eligibility

marks1 = int(input("Enter a marks of math :"))
marks2 = int(input("Enter a marks of physics :"))
marks3 = int(input("Enter a marks of chemistry :"))

total_marks = marks1 + marks2 + marks3
math_physices_total = marks1 + marks2 
if(marks1 >= 65 and
   marks2 >= 55 and
   marks3 >= 50 and
   total_marks >= 180 and
   math_physices_total >= 140):
    print("Yor are Eligible")
else:
    print("you are not Eligible")


