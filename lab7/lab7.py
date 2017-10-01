# Exercise 1: Write a Python function to sum all numbers in a list.

# 2nd way to generate a list
list = [i for i in range (1,5)]

# lets define the function now
def sumListItem(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum


# s = sumListItem(list)
# print(s)


# Exercise 2: Write a Python function to get the largest number from a list.

list = [i for i in range (1,10)]

def getMax(list):
    biggestsofar = 0
    for i in list:
        if i > biggestsofar:
            biggestsofar = i
    return biggestsofar

max = getMax(list)
print(max)

