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

# Q-6. Write a program to create a dictionary with 3 Hindi words as keys and their English translation as values. Allow the user to input a Hindi word and print its English Translation.

words = {
"madad" : "Help",
"Inshan" : "Human",
"loga" : "People"
}

word = input("Enter the word you want meaning of: ")

print(words[word])


# Q-7.Write a program to store 8 numbers in a set entered by the user and print the set.

s = set()
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))

print(s)

# Q-8. Write a program to check if a comment is spam or not. A comment is considered spam if it contains any of the following phrases:"make a lot of money", "buy now", "subscribe this", "click this". The program should take a comment as input and print "This comment is a spam" otherwise print "This comment is not a spam".

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment:")
 
if((p1 in message) or( p2 in message )or (p3 in message) or( p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")

# Q-9. Write a program to check if a given name is present in a list of names. The program should take a name as input and print "Name found" if the name is in the list, otherwise print "Name not found".

list = ["vedant", "Falguni", "Om", "mahima"]

name = input("Enter your name: ")

if(name in list):
    print("your name is in the list")

else:
    print("Your name is not in the list")