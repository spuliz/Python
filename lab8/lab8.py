# # Exercise 1:
# # Write a function to check if a key is present in a dictionary
# # – your function should take to parameters
# # – the key and the dictionary, and
# # return the value associated with the key, if present in the dictionary.
#
# variable = input("Insert a key ")
# my_dict = {'bill': '353-1234', 'rich': '269-1234', 'jane': '352-1234'}
#
# def check_key(my_dict, variable):
#         for key,value in my_dict.items():
#             if variable == key:
#                 return value
#             # else:
#         print("Key not present, try another key")
#         return None
#
# result = check_key(my_dict, variable)
# print(result)
#
#
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
#
#
# # Check Available amount
#
# search = input("Search an Item ")
# inventory = {'apple': 20, 'banana': 30, 'orange': 10}
#
# def checkAvailableAmount(inventory, search):
#     for key,value in inventory.items():
#         if search == key:
#             return value
#
#     print("0 - This item is not available at the moment.")
#
# itemsLeft = checkAvailableAmount(inventory, search)
# print(itemsLeft)

# Stock Up
inventory = {'apple': 20, 'banana': 30, 'orange': 10}

addItem1 = input("Item to update ")
updateItem1 = input("Insert the quantity to add ")
updateItem1 = int(updateItem1)

def stockUp(inventory, addItem, updateItem):
    for key, value in inventory.items():
        if addItem == key:
            inventory[key] = inventory[key] + updateItem
            return
    inventory[addItem] = updateItem

stockUp(inventory, addItem1, updateItem1)
print(inventory)



