#  Q-1. Write a program to find the largest of three number using if-else statement.

f = open("poem.txt")

content = f.read()
if("success" in content):
    print("The word success is present in this content")

else:
    print("The word success is not present in the content")


f.close()


# Q-2. Write a program to replace a word in a file with another word

word = "Anonymous"

with open("file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word,"######")

with open("file.txt","w") as f:
    f.write(contentNew)