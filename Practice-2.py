# Q-1. Write a python program to input student name and marks of 3 subject. print name & percentage in output.

name = input("Enter your Name :")
marks1 = int(input("Enter the marks of science :"))
marks2 = int(input("Enter the marks of Math :"))
marks3 = int(input("Enter the marks of English :"))

total_marks = marks1 + marks2 + marks3
percentage = (total_marks/300)*100

print(f" Name of Student : {name} ")
print(f"percentage : {percentage:.2f}% will done!")

# Q-2. write a python program that 