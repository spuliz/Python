## Exercise 1
def sum_all(list):
    sum = 0
    for i in range(0,len(list)):
        sum = sum + list[i]

    return sum

#Testing
#list = [1,2,3,4,5,6]
#print(sum_all(list))

##Exercise 2
def my_max(list):
    max = list[0];
    for i in range(1, len(list)):
        if list[i]>max:
            max = list[i]
    return max

#Testing
#list = [1,20,3,4,5,6]
#print(max(list))

##Exercise 3 - Write a Python function that takes a list of words
## and counts how many of them begin with ‘a’.

def count_a(list):
    count = 0
    for word in list:
        if word[0] == 'a':
            count+=1

    return count

#Testing
#list = ['hello', 'a', 'my', 'abracadabra', 'annie', 'john']
#print(count_a(list))


##Exercise 4: (modify Ex3) Write a Python function that takes a list of words and a character,
# and counts how many of the words in the list begin with that character.

def count_char(list, char):
    count = 0
    for word in list:
        if word[0] == char:
            count+=1

    return count

#Testing
# list = ['hello', 'a', 'my', 'abracadabra', 'annie', 'john']
# print(count_char(list, 'a'))
# print(count_char(list, 'm'))
# print(count_char(list, 'b'))



# Exercise 5: Write a Python function that takes a list of numbers and
# returns a new list containing only the even numbers from the first list.
# Hint: use list comprehension for the quickest solution

def even_numbers_only(list):
    #list of even numbers is initially empty
    even_numbers_list = []
    for i in list:
        if i%2==0:
            even_numbers_list.append(i)

    return even_numbers_list

#Testing
# list = [1,20,3,4,5,6,90,6,11,0]
# print(even_numbers_only(list))


#alternative solution using list comprehension
def even_numbers_only_v2(list):

    even_numbers_list = [n for n in list if n%2 == 0 ]
    return even_numbers_list

#Testing
# list = [1,20,3,4,5,6,90,6,11,0]
# print(even_numbers_only_v2(list))


