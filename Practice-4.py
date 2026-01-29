# Q-1. Limit the decimal place to 2 digit using .format method and print resultfor the variable pi = 3.14159265359

pi = 3.1417684956

print(round(pi,2))

print("value of pi is {}".format(pi))

print("value of pi is {:.2f}".format(pi))

# f-string
print(f"pi value is {pi:.2f}")

# Q-2. Extract charaters from index 2 to 8 with a step of 2: Given my_string ='Python course', slice charaters from index 2 to 8, skipping every other char

mystring = "python course"

print(mystring[2:8:2])

# Q-3. Slice to get only the middle charater(s): For my_string = 'Vedant' use slicing to extract the middle character(s)

mystring = "vedant"
# index     012345

mystring1 = "karan"
#            01234

# Function Method

def mid_str(word):
    middle = int(len(word)/2)
    if len(word) % 2 == 0:           # even char len
        return word[middle-1 : middle+1] #2:4
    else:                           # odd char len
        return word[middle]
    
print(mid_str(mystring))

# OR

my_string = 'Vedant'
middle = my_string[2:4]
print(middle)

# Q-4. Remove the first 3 and last 3 charaters: Given my string = 'Data Analysis',Remove the first 3 and last 3 char
    
str = "Data Analysis"
print(str[3:-3])


# Q-5. Get the substring that starts 4 characters from the end to the last character: for my_string = 'classification', slice the string starting from the 4th charater from the end to the charater.

str = "classification"
print(str[-4:])

# Q-6. How to Reverse a string using python string methods

word = "python"
print(word[::-1])

# Q-7. Write a python function to check if a string is a palindrome using string methods 
word = "madam"

def is_palindrome(s):
    if s == s[::-1]:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not palindrome")
    
is_palindrome(word)