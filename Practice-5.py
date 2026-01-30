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