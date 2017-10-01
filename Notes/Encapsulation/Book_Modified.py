# Example 4

# Extend the program from last week about the class Book and modify it so that
# it will create 5 books at run-time and add them to a list. Print the contents of
# the list

class Book:
    def __init__(self, ISBN, title, author):
        self.ISBN = ISBN
        self.title = title
        self.author = author
    def __str__(self):
        return "ISBN: {}, Title: {}, Author: {}".format(self.ISBN, self.title, self.author)

books = []

# populate the list
for i in range(5):
    id = input("Please enter the ISBN: ")
    t = input("Please enter the title: ")
    a = input("Please enter the author: ")
    b = Book(id, t, a);
    books.append(b)

# iterate over the list
for b in books:
    print(b)

