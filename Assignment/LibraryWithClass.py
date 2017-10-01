
#Library
class Library(object):
    def __init__(self, ID, type, title):
        self.ID = ID
        # self.type = type
        # self.title = title

    # def listOfItems(self):
    #     self.listOfItems = {self.ID:[self.title, self.type]}

    def listOfUsers(self, userID, userName):
        self.userID = userID
        self.userName = userName
        self.listOfUsers = {self.userID:[self.userName]}

    def addItem(self, ID, ):
        selection = int(input("Press 1 to add a book or press 2 to add a periodical "))
        if selection == 1:
            self.ID = int(input("Add ID "))
            for key in self.listOfBooks:
                if key == self.ID:
                    print("ID already exists ")
                    continue

    def removeItem(self):
        pass

    def addUser(self):
        pass

    def removeUser(self):
        pass

    def printItemsDetails(self):
        pass

    def printUsers(self):
        pass

#Your system should search using different parameters, e.g. name, not only search by id
    def searchBook(self):
        pass

    def searchUser(self):
        pass

#Books
class Book(Library):
    def __init__(self, ID, ISBN, title, Author, YearOfPublication):
        Library.__init__(self, ID, "Book", title)
        self.ID = ID
        self.ISBN = ISBN
        self.title = title
        self.Author = Author
        self.YearOfPublication = YearOfPublication
        self.Stock = []
        self.CopiesBorrowed = []
        self.CopiesAvailable = []

    def listOfBook(self):
        self.libraryBooks = {self.ID:[self.ISBN, self.Title, self.Author, self.YearOfPublication, self.Stock, self.CopiesBorrowed,
                                      self.CopiesAvailable]}

    def borrowBook(self, library):
        self.ISBN = int(input(" Insert ISBN to borrow "))
        self.CopiesBorrowed = int(input("Add Copies Borrowed "))

    def returnBook(self, library):
        self.ISBN = int(input(" Insert ISBN to borrow "))
        self.CopiesReturned = int(input("Add Copies Returned "))

    def addBook(self, library):
        while True:
            self.ID = int(input("Add ID "))
            for key in self.libraryItems:
                if key == self.ID:
                    print("ID already exists ")
                    continue
            else:
                self.ISBN = input("Add the ISBN")
                self.Author = input("Insert the full name of the author: ")
                self.Title = input("Insert title: ")
                self.Stock = int(input("Add the number of copies purchased: "))
                self.CopiesBorrowed = 0
                self.CopiesAvailable = addStock
                add_book(library1, addISBN1, addAuthor1, addTitle1, addStock1, addCopiesBorrowed1, addCopiesAvailable1)
                break

        self.ISBN = int(input("Add ISBN "))
        self.Title = input("Add Title ")
        self.Author = input("Add Author ")
        self.YearOfPublication = input("Add Year of Publication ")
        self.Stock = int(input("Add Copies Borrowed "))
        self.CopiesAvailable = int(input("Add Title "))


#Periodicals
class Periodical(Library):
    def __init__(self, ID, Title, Editor, YearOfPublication, Volume, Issue):
        Library.__init__(self, ID, "Periodical", title)
        self.ID = ID
        self.title = title
        self.Editor = Editor
        self.YearOfPublication = YearOfPublication
        self.Volume = Volume
        self.Issue = Issue

#Users
class User(object):
    def __init__(self, userID, name, address):
        self.userID = userID
        self.name = name
        self.address = address
        self.onLoan = [] #a list of books borrowed


library1 = library()
print(library1.libraryBooks)
