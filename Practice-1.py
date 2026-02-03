# Q-1. Write a Python program that print the following text.
'''Python is fun. 
"Quotes" and 'single Quotes' can be tricky'''


print('''Python is fun.\n "Quotes" and 'single Quotes' can be tricky''')


# Q-2 Create 3 variables to store Name,age and city. Then print a sentence that uses these variables.

name = "vedant"
age = 20
city = "Nagpur"
print("My name is",name, "and my age is",age,"i am living in",city)

#    OR

print(f"my name is {name} and my age is {age} i am living in {city}") # this is f string 

# Q-3. Write a program to print Twinkle Twinkle little star poem using in python.

print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.''')


# Q-4. Write a program to add two numbers and print the result.

a = 56
b = 78

print(a + b)

# Q-5. Write a program to find the remainder when a is divided by b.

a = 18
b = 6

print("remainder when a is divided by b is",a % b)

# Q-6. Write a program to convert a string to a float and print the type.

a = input("enter the value of a:")
t = float(a)
print(type(t))

# Q-7. Write a program to check if a is grater than b by inputing two numbers from input function.

a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))

print("a is greater than b is ", a>b)

# Q-8. Write a program to find the avrage of two numbers entered by the user.

a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))

print(" the average of these two number is ",(a+b)/2)

# Q-9. write a program to calculate the square of a number entered by the user.
a = int(input("Enter  your number :"))

# Squaring for the Number
print ("the square of the number is ", a**2)
print ("the square of the number is ", a*a)
