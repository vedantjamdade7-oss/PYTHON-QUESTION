# Q-1. print the while loop output in same line 

i = 1
while i < 4:
    print(f" Hey{i}", "vedant", sep = "-",end = " ")
    i  += 1
    # end is used for to create all variable in one line like,
    # (output = hey vedant 1  hey vedant 2  hey vedant 3 )
    # sep is used for seprated the value and any function for saprated

# Q-2. Print star patterns - Using loops

# star 

n = 5

for i in range (1,n+1):
    for j in range (1,i+1):
       print("*",end = " ")
    print()

# Q-3. Write a program to find the factorial of a given number

def factorial(n):
    result = 1
    while n > 0:
        result *=n
        n -= 1
    return result

print(factorial(8))

# Q-4. Count the number of vowels in a string (vowels a,e,i,o,u)

string = "python by vedant jamdade you know he is a legent"
vowels = "aeiou"
count = 0

for char in string:
    if char.lower() in vowels:
        count += 1
print("Number of vowels are",count)

# Q-5. Find the longest word in a sentence using a for loop

string = "python by vedant jamdade you know he is a legent"
words = string.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word is:", longest_word)

# Q-6. "do while" Loop in python - how to do it.

while True: 
    num = int(input("Enter a number greater than 10:"))
    if num > 10:
        print(f"valid number entered: {num}")
        break
    else:
        print("number is not greater than 10, try again")

# Q-7. Write a program to print first N number in the Fibonacci using while loop.

def fibonacci(n):
    a,b = 0,1
    count = 0
    while count < n:
        print(a)
        a,b = b , a+b
        count += 1
        
fibonacci(10)