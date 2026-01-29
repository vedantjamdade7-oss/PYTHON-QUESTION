# Q-1. print the while loop output in same line 

i = 1
while i < 4:
    print(f" Hey{i}", "vedant", sep = "-",end = " ")
    i  += 1
    # end is used for to create all variable in one line like,
    # (output = hey vedant 1  hey vedant 2  hey vedant 3 )
    # sep is used for seprated the value and any function for saprated