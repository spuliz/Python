# Exercise 1
# Write a function that takes a number as a parameter and prints the numbers from 1 to that number on the screen.

def series (a):
    for i in range(1,a+1):
        print(i, end="")
    print()

# a = input("Insert a number ")
# a = int(a)
# series(a)

# Exercise 2
# Write a function that takes a number as a parameter and iterates from 0 to that number.
# For each iteration, it will check if the current number is even or odd, and report that
# to the screen (e.g. "1 is odd, 2 is even").

def even_odd (a):
    for i in range(0,a+1):
        if i%2 == 0:
            print(i, "Is even")
        else:
            print(i, "Is odd")

# a = input("Insert a number ")
# a = int(a)
# even_odd(a)

# Exercise 3: Write a function that takes a number as a parameter, iterates from 0 to that number,
# and for each iteration of the loop, multiplies the current
# number by 9 and prints the result (e.g. "2 * 9 = 18").

def multiplier (a):
    for i in range(0,a+1):
        i = i * 9
        print(i)

# a = input("Insert a number ")
# a = int(a)
# multiplier(a)

# Exercise 4: Write a function that asks the user for a number and
# prints the sum of all numbers from 1 to the number they enter.

def sum (a):
    c = 0
    for i in range(1,a+1):
        c = c + i
    print(c)

# a = input("Insert a number ")
# a = int(a)
# sum(a)

# Exercise 5: Write a function to print a factorial of a number.

def factorial (a):
    c = 1
    for i in range (1, a+1):
        c = c * i
    print(c)

# a = input("Insert a number ")
# a = int(a)
# factorial(a)

# Exercise 6: Write a function that takes a string as a parameter and returns a string that is made up of the first
# two characters and the last two characters. If the string has a length less than 4
# the program prints a message on the screen.
# For example: “hello there” will result in “here”

def string (a):
    for char in (a):
        if len(a) < 4:
            print("String is too short")
        else:
            result = a[:2]+a[-2:]
    print(result)
# a = input("Insert a string ")
# string(a)

# Exercise 7: Write a Python program to remove the characters which
# have odd index values of a given string

def clean (a):
    new_string = ""
    for index in range(0,len(a)):
        if index%2 == 0:
            new_string = new_string + a[index]

    print(new_string)
# a = input("Insert a string ")
# clean(a)

# Exercise 8: Write a Python function to get the first half of a specified string of even length
# Sample function and result:
# string_first_half('Python') -> Pyt

def halfstring (a):
    new_string = ""
    for c in range(0, len(a)):
        if len(a)%2 == 0:
            new_string = a[:len(a)//2]
        else:
            print("The string you enter is not even")
            break
    print(new_string)
# a = input("Insert a string of even length ")
# halfstring(a)

# Exercise 9: Write a Python function to insert a string in the middle of a string. Sample function and result:
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
def insert_string_middle (a):
    new_string = ""
    for c in range (0, len(a)):
        new_string = b[0:len(b)//2] + a + b[len(b)//2:]
    print(new_string)
# a = input("Insert a string ")
# b = input("Insert the middle string ")
# insert_string_middle(a)


# Exercise 10: Write a Python function that takes a string and two indices, and returns a string
# with the part between the indices removed.
# For example: remove_substring(“Hello there”, 2, 6) -> “Hehere”

b = input("Insert the first index")
b = int(b)
c = input("Insert the second index")
c = int(c)
def remove_substring (a):
    new_string = ""
    for c in range (0, len(a)):
        new_string = a[0:b] + a[c:]
    print(new_string)
a = input("Insert a string ")
remove_substring(a)

