#  Q-1. Write a program to find the largest of three number using if-else statement.

f = open(r"d:\GitHub_QA\PYTHON-QUESTION\poem.txt")

content = f.read()
if("success" in content):
    print("The word success is present in this content")

else:
    print("The word success is not present in the content")


f.close()