# Student Name: Saverio Pulizzi
# Student ID: D16125207
# Labtest 2 - 6th Dec 2016

# a) Write a Python function replace_all which replaces all occurrences of a list of words with
#    other words in a string. The function should have three parameters: (1) the string, (2) the list
#    of words to be replaced, and (3) the list of words to be replaced with


sentence = 'This is a beautiful day'
# converting the sentence into a list
list = sentence.split()
list1 = ['is']
list2 = ['was']

def replace_all(list, list1, list2):
    for word in list:
        if word == list1[0]:
            # searching for the index and replacing it with the new word
            list[list.index(word)] = list2[0]
            # changing the list into a string
            sentence = ' '.join(list)
            print(sentence)
            return sentence
    print("This word is not present in the sentence")

replace_all(list,list1,list2)



# Write a Python program that will read from a file, replace all occurrences of some words
# with other words, and write the result in a different file. This program will use the function
# replace_all( ) you’ve written in part (a).

# here I have created my list from the input file

def create_list():
    fo = open("text", "r")
    list = []
    for line in fo:
        line = line.lower()
        line = line.split()
        print(line)
    fo.close()
    return list

# here I have defined the function above
def replace_all(list, list1, list2):
    for word in list:
        if word == list1[0]:
            list[list.index(word)] = list2[0]
            sentence = ' '.join(list)
            print(sentence)
            return sentence
    print("This word is not present in the sentence")

# here I have created the function to write the output
def create_output(list):
    fo = open("output.txt", "w")
    fo.write("end")

list = create_list()
replace = replace_all(list, ['seven'], ['eight'])
create_output(list)


