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


# Q-3. Write a program to store seven fruites in a list entered by the user and print the list.
fruits = []
f1 = input("Enter fruits name:")
fruits.append(f1)
f2= input("Enter fruits name:")
fruits.append(f2)
f3 = input("Enter fruits name:")
fruits.append(f3)
f4 = input("Enter fruits name:")
fruits.append(f4)
f5 = input("Enter fruits name:")
fruits.append(f5)
f6 = input("Enter fruits name:")
fruits.append(f6)
f7 = input("Enter fruits name:")
fruits.append(f7)


# Q-4. Write a program to store marks of six subjects entered by the user in a list and print the sorted list of marks.

marks = []
f1 = int(input("Enter marks Sci:"))
marks.append(f1)
f2 = int(input("Enter marks Math:"))
marks.append(f2)
f3 = int(input("Enter marks Eng:"))
marks.append(f3)
f4 = int(input("Enter marks Hindi:"))
marks.append(f4)
f5 = int(input("Enter marks SST:"))
marks.append(f5)
f6 = int(input("Enter marks Computer:"))
marks.append(f6)

marks.sort()
print(marks)

# Q-5. Write a program to store five friends name and their favorite language in dictionary entered by the user.

d = {}

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

print(d)