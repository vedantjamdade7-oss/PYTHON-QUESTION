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


# Q-3. Write a program to check if the word "python" is present in the file or not.

with open("log.txt") as f:
    content = f.read()

if("Python" in content):
    print("Yes Python is Present")
else:
    print("No Python is not present")
    

# Q-4. Write a program to check if the word "Python" is present in the file or not and also print the line number if it is present.

with open("log.txt") as f:
    lines = f.readlines()  # Correct variable name

lineno = 1
for line in lines:
    if "python" in line.lower():  # Optional: .lower() for case-insensitive
        print(f"Yes, 'python' is present. Line no: {lineno}")
        break
    lineno += 1
else:
    print("No, 'python' is not present.")


# Q-5. Write a program to copy the content of one file to another file.
with open("this.txt") as f:
    Content = f.read()

with open("this_copy.txt","w") as f:
    f.write(Content)

# Q-6. Write a program to create a game in which you have to guess a number between 1 to 100 and you will be given a score based on how close you are to the actual number. The score will be calculated as 100 - the absolute difference between your guess and the actual number.
import random

def game():
    print("You are playing the game..")
    score = random.randint(1, 100)

    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open("hiscore.txt","w") as f:
            f.write(str(score))

    return score    

game()    
        


