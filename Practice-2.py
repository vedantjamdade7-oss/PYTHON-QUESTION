# Q-1. Write a python program to input student name and marks of 3 subject. print name & percentage in output.

name = input("Enter your Name :")
marks1 = int(input("Enter the marks of science :"))
marks2 = int(input("Enter the marks of Math :"))
marks3 = int(input("Enter the marks of English :"))

total_marks = marks1 + marks2 + marks3
percentage = (total_marks/300)*100

print(f" Name of Student : {name} ")
print(f"percentage : {percentage:.2f}% will done!")

# Q-2. write a python program that collects multiple types of data (e.g., name, age, height,and student status) from user input, stores them in a dictionary,and then print out the collection data?

# initializing a Dictionary
user_data = {}

# input from user
user_data['name'] = input("Enter your Full Name :")
user_data['age'] = int(input("Enter your age :"))
user_data['height'] = float(input("Enter your height :"))
user_data['status'] = input("Enter your statues :")

print(user_data)