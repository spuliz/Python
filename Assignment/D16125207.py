# Library
class Library(object):
    def __init__(self, library_name):
        self.library_name = library_name
        self.users = []
        self.books = []
        self.periodicals = []

    def loan_or_return_a_book(self):
        '''function defined to loan or return a book'''
        print("\nPlease, press 1 to borrow a book or 0 to exit")
        menu = {}
        menu['2'] = "--> Return a book"
        menu['1'] = "--> Borrow a book"
        menu['0'] = "--> Exit"
        sorted_options = sorted(menu.keys())
        for entry in sorted_options:
            print(entry, menu[entry])
        while True:
            selection = input("\nPlease enter an option number or press zero to exit:")
            if selection == '1':
                    try:
                        self.isbn = input("Please insert the ISBN of the book that you want to borrow: ")
                        if len(self.isbn) < 13:
                            print("ISBN too short")
                            continue
                        elif len(self.isbn) > 13:
                                print("ISBN too long")
                                continue
                        else:
                            self.isbn = int(self.isbn)
                            for b in self.books:
                                if self.isbn == b["Book ISBN"]:
                                    break
                            else:
                                print("ISBN does not exist")

                            try:
                                self.isbn = int(self.isbn)
                                for b in self.books:
                                    if self.isbn == b["Book ISBN"]:
                                        self.user = int(input("Insert userID: "))
                                        for u in self.users:
                                            if self.user == u["User ID"]:
                                                if self.isbn in u["Items on loan"]:
                                                    print("Book already borrowed")
                                                    break
                                                else:
                                                    u["Items on loan"].append(self.isbn)
                                                    print(b["Book Title"], "successfully borrowed by:", u["Name"])
                                                    break
                                        else:
                                            print("UserID does not exist")
                                            break
                            except:
                                print("Invalid ISBN please try again.")
                                continue
                    except:
                        print("Invalid ISBN please try again")
                        continue

            elif selection == '0':
                break

            elif selection == '2':
                try:
                    self.isbn = input("Please insert the ISBN of the book that you want to return: ")
                    if len(self.isbn) < 13:
                        print("ISBN too short")
                        continue
                    elif len(self.isbn) > 13:
                            print("ISBN too long")
                            continue
                    else:
                        self.isbn = int(self.isbn)
                        for b in self.books:
                            if self.isbn == b["Book ISBN"]:
                                break
                        else:
                            print("ISBN does not exist")

                        try:
                            self.isbn = int(self.isbn)
                            for b in self.books:
                                if self.isbn == b["Book ISBN"]:
                                    self.user = int(input("Insert userID: "))
                                    for u in self.users:
                                        if self.user == u["User ID"]:
                                            if self.isbn in u["Items on loan"]:
                                                u["Items on loan"].remove(self.isbn)
                                                print(b["Book Title"], "has been removed", "from", u["Name"])
                                                break
                                            else:
                                                print(b["Book Title"], "is not in", u["Name"], "'s list of borrowed books")
                                                break
                                    else:
                                        print("UserID does not exist")
                                        break
                        except:
                            print("Invalid ISBN please try again.")
                            continue
                except:
                    print("Invalid ISBN please try again")
                    continue

            else:
                print("The option you have selected does not exist, please try again.")


    def add_user(self, u):
        '''function to add a new user to the library'''
        self.users.append(u)

    def add_book(self, b):
        '''function to add a new book to the library'''
        self.books.append(b)

    def add_periodical(self, p):
        '''function to add a new periodical to the library'''
        self.periodicals.append(p)

    def remove_user(self, u):
        '''function to remove a user from the library'''
        self.users.remove(u)

    def remove_book(self, b):
        '''function to remove a book from the library'''
        self.books.remove(b)

    def remove_periodical(self, p):
        '''function to remove a periodical from the library'''
        self.periodicals.remove(p)

    def search_book(self, query):
        '''function to search for a book into the library'''
        self.query = query
        for d in self.books:
            if self.query in d.values():
                break
        else:
            print("No books were found for your search")
        for d in self.books:
            if self.query in d.values():
                for value in d.values():
                    if self.query == value:
                        print("\nThose are the book's details as a result of your search -->", "Library ID:", d["Library ID"], "|", "Title:", d["Book Title"],"|",
                              "Author:", d["Book Author"],"|", "ISBN:", d["Book ISBN"],"|", "Year of publication:", d["Year of publication"])
                        break

    def search_user(self, query):
        '''function to search for a user registered in the library'''
        self.query = query
        for d in self.users:
            if self.query in d.values():
                break
        else:
            print("No users were found for your search")
        for d in self.users:
            if self.query in d.values():
                for value in d.values():
                    if self.query == value:
                        print("\nThose are the user's details as a result of your search -->", "User ID:", d["User ID"], "|", "Name:", d["Name"],"|",
                              "Address:", d["Address"],"|", "Items on loan:", d["Items on loan"])
                        break

    def list_of_items(self):
        print("This is the list of books:")
        for d in self.books:
            print("Library ID:", d["Library ID"], "|", "Title:", d["Book Title"],"|",
                  "Author:", d["Book Author"],"|", "ISBN:", d["Book ISBN"],"|", "Year of publication:", d["Year of publication"])
        print("\nThis is the list of periodicals:")
        for d in self.periodicals:
            print("Library ID:", d["Library ID"], "|", "Title:", d["Title"],"|",
                  "Editor:", d["Editor"],"|", "Year of publication:", d["Year of publication"],"|", "Volume:", d["Volume"],"|", "Issue:", d["Issue"])

    def list_of_users(self):
        print("This is the list of users:")
        for d in self.users:
            print("User ID:", d["User ID"], "|", "Full Name:", d["Name"],"|",
                  "Address:", d["Address"],"|", "List of items on loan:", d["Items on loan"])



# Book
class Book(Library):

    def __init__(self, library_name, library_id, isbn, title, author, year_of_publication):
        super(Book, self).__init__(library_name)
        self.library_id = library_id
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.books = {"Name of the library": library_name, "Library ID": library_id, "Book ISBN": isbn, "Book Title": title, "Book Author": author,
                      "Year of publication": year_of_publication}


# Periodical
class Periodical(Library):
    def __init__(self, library_name, library_id, title, editor, year_of_publication, volume, issue):
        super(Periodical, self).__init__(library_name)
        # inheritance can be applied between periodicals and books
        self.library_id = library_id
        self.title = title
        self.editor = editor
        self.year_of_publication = year_of_publication
        self.volume = volume
        self.issue = issue
        self.periodicals = {"Library name": library_name, "Library ID": library_id, "Title": title, "Editor": editor, "Year of publication": year_of_publication,
                            "Volume": volume, "Issue": issue}

# User
class User(Library):
    def __init__(self, library_name, user_id, name, address):
        super(User, self).__init__(library_name)
        self.user_id = user_id
        self.name = name
        self.address = address
        self.items_on_loan = []
        self.users = {"User ID": user_id, "Name": name, "Address": address, "Items on loan": self.items_on_loan}


# Instance of library
l = Library("DIT Library")

# Instances of books
b1 = Book("DIT Library", 1,1234567890123,"Python", "Lynda", 2011)
b2 = Book("DIT Library", 2,1234567890124,"PHP", "Udemy", 2012)
b3 = Book("DIT Library", 3,1234567890125,"Java", "Codeacademy", 2010)

# Instances of periodicals
p1 = Periodical( "DIT Library", 4,"New York Times","Dean Baquet",2005,10,4)
p2 = Periodical( "DIT Library", 5,"Science","Jeremy M. Berg",2011,8,6)
p3 = Periodical( "DIT Library", 6,"Times","John Witherow",2016,10,4)

# Instances of users
u1 = User("DIT Library",10, "Saverio Pulizzi", "Upper Sheriff Street")
u2 = User("DIT Library", 11, "John Buckley", "Grand Canal Square")
u3 = User("DIT Library", 12, "Mohammed Hassouni", "Grafton Street")

# Adding the book instances into our library
l.add_book(b1.books)
l.add_book(b2.books)
l.add_book(b3.books)

# Adding the periodical instances into our library
l.add_periodical(p1.periodicals)
l.add_periodical(p2.periodicals)
l.add_periodical(p3.periodicals)

# Adding user instances into our library
l.add_user(u1.users)
l.add_user(u2.users)
l.add_user(u3.users)

# Printing the list of items
print(l.list_of_items())

#Printing the list of users
print(l.list_of_users())

# Loan or return a book
l.loan_or_return_a_book()

#Searching for a book using the book title
l.search_book("Python")

#Searching for a user using its ID
l.search_user(11)

#Removing user u1
l.remove_user(u1.users)
