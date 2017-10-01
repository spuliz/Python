# # Exercise 1: Write a function that takes a number as a parameter and
# # prints the numbers from 1 to that number on the screen.
#
# n = input("Insert a number ")
# n = int(n)
#
# def series(n):
#     i = 1
#     print(i)
#     for i in range(i,n):
#         i += 1
#         print(i)
#
# new_series = series(n)
#
#
#
# # Exercise 2: Write a function that takes a number as a parameter and
# # iterates from 0 to that number. For each iteration, it will check if the current number
# # is even or odd, and report that to the screen (e.g. "1 is odd, 2 is even").
#
# n = input("Insert a number ")
# n = int(n)
#
# def iteration(n):
#     for i in range(0,n+1):
#         if i%2 == 0:
#             print("Even")
#         else:
#             print("Odd")
#
# my_print = iteration(n)
#
#
# # Exercise 3: Write a function that takes a number as a parameter, iterates from 0 to that number,
# # and for each iteration of the loop, multiplies the current number by 9 and prints the result (e.g. "2 * 9 = 18").
#
# n = input("Insert a number ")
# n = int(n)
#
# def multipler(n):
#     for i in range(0,n+1):
#         print('{} * 9 = {}'.format(i, i*9))
#
# my_print = multipler(n)
#
#
#
# # Exercise 4: Write a function that asks the user for a number and prints the sum of all numbers
# # from 1 to the number they enter.
#
# n = input("Insert a number ")
# n = int(n)
#
# def series(n):
#     i = 1
#     print(i)
#     for i in range(i,n):
#         i += 1
#         print(i)
#
# new_series = series(n)
#
# # Exercise 5: Write a function to print a factorial of a number.
#
# n = input("Insert a number ")
# n = int(n)
#
# def factorial(n):
#     result = 1
#     for i in range(1,n):
#         i += 1
#         result = result * i
#     print(result)
#
# my_print = factorial(n)


# Exercise 6: Write a function that takes a string as a parameter and
# returns a sting that is made up of the first two characters and the last two characters.
# If the string has a length less than 4 the program prints a message on the screen.
# For example: “hello there” will result in “here”

# s = input("Insert a string ")
#
# def newString(s):
#     if len(s) <= 4:
#         print("Too short")
#         return ""
#     else:
#         return s[:2] + s[-2:]
#
# my_print = newString(s)
# print(my_print)

# Music Notation

# def musicNotation():
#     fo = open("hnr","r")
#     new_string = ""
#     for line in fo:
#         line = line.strip()
#         for c in line:
#             if c == 'X':
#                 index = line[2:] + ' ... '
#             elif c == 'T':
#                 title = line[2:]
#                 break
#             elif c == 'M':
#                 time = line[2:]
#             elif c == 'K':
#                 signature = line[2:]
#                 print(index,title,"...","Time sig:", time, "...","Key sig:",signature,"...")
#     fo.close()
#     return new_string
#
#
# my_print = musicNotation()


# Exercise 1: Write a Python function to sum all numbers in a list.

# user_input = input("Please provide list of numbers separated by comma, e.g. 1,2,3: ")
# list = list(map(int,user_input.split(',')))
#
# def sumList(list):
#     result = 0
#     for element in list:
#         result = result + element
#     print(result)
#
# my_print = sumList(list)

# Exercise 2: Write a Python function to get the largest number from a list. 

# user_input = input("Please provide list of numbers separated by comma, e.g. 1,2,3: ")
# list = list(map(int,user_input.split(',')))
#
# def my_max(list):
#     max = list[0];
#     for i in range(1, len(list)):
#         if list[i]>max:
#             max = list[i]
#
#     return max
#
# result = my_max(list)
# print(result)

##Exercise 3 - Write a Python function that takes a list of words
## and counts how many of them begin with ‘a’.

# user_input = input("Please provide list of words separated by comma, e.g. io,sono,gio: ")
# list = list(map(str,user_input.split(',')))
#
# def countWord(list):
#     count = 0
#     for element in list:
#         if element[0:1] == 'a':
#             count = count + 1
#     return count
#
# result = countWord(list)
# print(result)

##Exercise 4: (modify Ex3) Write a Python function that takes a list of words and a character,
# and counts how many of the words in the list begin with that character.

# user_input = input("Please provide list of words separated by comma, e.g. io,sono,gio: ")
# character = input("Insert a character: ")
# list = list(map(str,user_input.split(',')))
#
#
# def countWord(list):
#     count = 0
#     for element in list:
#         if element[0:1] == character:
#             count = count + 1
#     return count
#
# result = countWord(list)
# print(result)


# Exercise 5: Write a Python function that takes a list of numbers and
# returns a new list containing only the even numbers from the first list.
# Hint: use list comprehension for the quickest solution

# user_input = input("Please provide list of numbers separated by comma, e.g. 1,2,3: ")
# list = list(map(int,user_input.split(',')))
#
# def countWord(list):
#     new_list = []
#     for element in list:
#         if element%2 == 0:
#             new_list.append(element)
#     return new_list
#
# result = countWord(list)
# print(result)

#Exercise 1: Write a function to check if a key is present in a dictionary –
# your function should take to parameters – the key and the dictionary,
# and return the value associated with the key, if present in the dictionary.

# variable = input("Insert a key ")
# my_dict = {'bill': '353-1234', 'rich': '269-1234', 'jane': '352-1234'}
#
# def getValue(x,dict):
#     for current_key in dict.keys():
#         if current_key == x:
#             return dict[current_key]
#     return none
#
# value = getValue(variable, my_dict)
# print(value)

# # Exercise 3: Write a small shopping program. We’ll use a dictionary to hold the inventory – items and quantity:
# # inventory = { ‘apple’:20, ‘banana’:30, ‘orange’:10}
# # Write functions in Python to:
# # Check available amount
# # The function amount should take two parameters – item to search and the dictionary,
# # and return the quantity available, or 0 if none.
# # For example,
# # amount(‘apple’ inventory) should return 20
# # add stock, for example stock_up(‘apple’,10) should result in the inventory being updated with 10 extra apples
# # inventory will be  { ‘apple’:30, ‘banana’:30, ‘orange’:10}
# #
# # You have to search through the inventory first to see if item is available
# # if available – update the quantity plus the new amount
# # if not available - add it with the specified quantity
# #
# # print all stock – print all items in stock and their quantity

# variable = input("Search for a product ")
# inventory = {'apple': 20, 'banana': 30, 'orange': 10}
#
# def checkAvailableAmount(x, dict):
#     for current_key in dict.keys():
#         if current_key == x:
#             return dict[current_key]
#         else:
#             return 0
#
# value = checkAvailableAmount(variable, inventory)
# print(value)

# Stock up
inventory = {'apple': 20, 'banana': 30, 'orange': 10}
addItem = input("Item to update ")
updateItem = input("Insert the quantity to add ")
updateItem = int(updateItem)


def addStock(inventory, addItem, updateItem):
    for key, value in inventory.items():
        if addItem == key:
            inventory[key] = inventory[key] + updateItem
            return
    inventory[addItem] = updateItem #we add a new product

addStock(inventory, addItem, updateItem)
# print(inventory)

def print_all_stock(inventory):
    for key in inventory.keys():
        print('Item: {}, Quantity: {}'.format(key, inventory[key]))

result = print_all_stock(inventory)
print(result)


# def create_dict():
#     fo = open("text","r")
#     dict = {}
#     for line in fo:
#         line = line.lower()
#         line = line.split()
#         print(line)
#         for w in line:
#             word_frequency(w,dict)
#     fo.close()
#     return dict
#
#
# def word_frequency(word, dict):
#     for key in dict.keys():
#         if key == word:
#             dict[key] = dict[key] + 1
#             return dict
#         else:
#             dict[key] = 1
#             return dict
#
# dict = create_dict()



