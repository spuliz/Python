# Ex1 Write a Python program to print each character of a string on single line.
s = input('Please enter a string:')
print('You have entered:')
for c in s:
    print(c)

# Ex2 Write a Python program that will calculate the length of a string (we already have a function len that does that,
# but we want to implement our own)
s = input('Please enter a string:')
print('The lenght of your string is:')
i= 0
for c in s:
    i = i + 1
print(i)

#Exercise 3: Write a Python program that reads a string and prints a sting that is made up
# of the first two characters and the last two characters.
# If the string has a length less than 4 the program prints a message on the screen.
#For example: “hello there” will result in “here”

s = input("Please enter a string: ")
if len(s) < 4:
    print("String is too short")
else:
    result = s[0:2]+s[-2:]
    print("Result: ", result)

#Exercise 4: Write a Python program that will reverse a string (using a loop)

s = input("Please enter a string: ")
reversed_s = ""
for c in s:
    reversed_s = c + reversed_s
print("Reversed string is: ", reversed_s)

#Exercise 5: Write a Python program that will “encrypt” a string.
#The encryption algorithm we’ll use is add 1 to the ASCII code, so ‘a’ becomes ‘b’, ‘b’ becomes ‘c’, etc.
# The string ‘abc’ becomes ‘bcd’
#You’ll need to use the functions ord() and chr() discussed in class
#Hint: To encrypt the letter ‘a’ take the ASCII code of ‘a’ -97, add 1 (98)
# and find the character with ASCII code 98 (‘b’). So ‘a’ encrypted becomes ‘b’

s = input("Please enter a string: ")
encrypted_s = ""
for c in s:
    new_c = chr(ord(c) + 1) # new_c is the encrypted character c
    encrypted_s = encrypted_s + new_c
print("Encrypted string: ", encrypted_s)

#Exercise 6: Write a Python program that will swap two random letters in a string.
#Hint: Random letters means “letters with random index”
# random.randint(x,y) will return a random number in the range from x to y inclusive.
# You need to import random at the top of your program.
# You’ll also need to use slicing – splitting your string into substrings.

import random

s = input("Please enter a string: ")

i = random.randint(0,len(s))  # generate a random number to represent the index of the 1st letter to swap
j = random.randint(0,len(s))  # generate a random number to represent the index of the 2nd letter to swap

# We want to swap the letters at index i and index j
# We will make the assumptions that
# 1. i and j are different - if not generate a different j
# 2. i is smaller than j - if not, swap the values of i and j

#1. Ensure that i and j are different
while (j == i):
    j = random.randint(0,len(s)) # generate a new j. Keep generating a new j until it is different than i

#2. Ensure i < j
if i> j:
    i, j = j, i    #swap the values for i and j. Remember multiple assignment from the first lecture?

#Swap the letters at index i and index j
#To do that we will slice the string to everything on the left of index i,
# the string between i and j, and the string on the right of j
#For example, if our string is "abracadabra" and we have i = 2 (character "r") and j = 8 (character "b")
# we will slice it as "ab" + "r" + "acada" + "b" + "ra"
# and re-build  new string but swapping "r" and "b"
#
#The slicing will look like
# s[0:i] (string "ab") + s[i] ("r") + s[i+1:j] ("acada") + s[j] ("b") + s[j+1:] ("ra")

result_s = s[0:i] + s[j] + s[i+1 : j] + s[i] + s[j+1:]
print("Result: " + result_s)
print("Characters swapped: ", s[i], " and ", s[j])
