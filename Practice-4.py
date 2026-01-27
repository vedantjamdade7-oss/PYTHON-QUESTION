# Q-1. Limit the decimal place to 2 digit using .format method and print resultfor the variable pi = 3.14159265359

pi = 3.1417684956

print(round(pi,2))

print("value of pi is {}".format(pi))

print("value of pi is {:.2f}".format(pi))

# f-string
print(f"pi value is {pi:.2f}")



# Get the substring that starts 4 characters from the end to the last character: for my_string = 'classification', slice the string starting from the 4th charater from the end to the charater.