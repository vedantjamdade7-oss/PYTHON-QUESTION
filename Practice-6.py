# Q-1. Find the intersection (common element) of two lists

# list , tuple, set and dict
# data structures / collection


list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

def intersection_loop(lst1,lst2):
    common_list = []
    for item in lst1:
        if item in lst2 and item not in common_list:
            common_list.append(item)
    return common_list
# print(intersection_loop(list1,list2))

# using list comprehension

def intersection_comp (list1,list2): # def is a function 
    return [item for item in list1 if item in list2] # item is just a variable name,item in lst1 checking the item[1,2,3,4],if in list2 
print(intersection_comp(list1,list2))

# Q-2. Find the most Frequent Elemnt in a list

number = [1,2,2,3,3,3,4,4]

def common_num (lst):
    max_count = 0
    most_freq = None
    for item in lst:
        count = lst.count(item)
        if count > max_count:
            max_count = count
            most_freq = item
    return most_freq
   
print(common_num(number))

# Q-3. Find cumulative sum of a list.

number = [1,2,3,4]

def cumulative_sum(lst):
    cum_sum = []
    total = 0
    for num in lst:
        total += num
        cum_sum.append(total)
    return cum_sum
print(cumulative_sum(number))


cumulative = [  sum(number[:x + 1]) for x in range(len(number)) ]
print(cumulative)

# Q-4.  Remove Duplicates from a list - 2 Methodes

# Methode-1

fruits = ["apple", "banana", "cherry", "apple","banana"]

# using loop
# use in real word lack of list present there

# def remove_duplicates(lst):
#     unique = []
#     seen = set()
#     for item in lst:
#         if item not in seen:
#             unique.append(item)
#             seen.add(item)
#     return unique
# print(remove_duplicates(fruits))

# Methode-2

def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
       
    return unique
# print(remove_duplicates(fruits))

# using set constructor
print(list(set(fruits)))

# Q-5. Find the index of an element in a tuple

my_tuple = (1,2,3,4)
def find_index(tup,elem):
    return tup.index(elem) if elem in tup else 'nahi hai '

print(find_index(my_tuple,1000))

# Q-6. Find the most frequent value in a dictionary

data = {'a':1, 'b':2, 'c':1, 'd':3, 'e':1}

def common_value (dict):
    frequency = {}
    for value in dict.values():
        if value not in frequency:
            frequency[value] = 0
        frequency[value] += 1
    max_value = max(frequency , key=frequency.get)
    return max_value
print(common_value(data))

# Q-7. Merge Dictionaries with summation

dict1 = {'a':10, 'b':20, 'c':30}
dict2 = {'b':15, 'c':35, 'd':25}

def merge_dict(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

print(merge_dict(dict1,dict2))

