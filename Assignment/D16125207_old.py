# Library hardcoded

library1 = {1234567890123:['Saverio Pulizzi', 'Intro to Python', 3, 0, 3], 1234567890124:['John Smith', 'Intro to PHP', 3, 0, 3],
            1234567890125:['Mary Land', 'Intro to Java', 3, 0, 3]}


def print_detail(library):
    ''' function to print all the book details '''
    for key, value in library.items():
        print(key,'-->','author:',library[key][0],'|', 'title:',library[key][1],'|', 'Stock:',library[key][2],'|', 'Copies Borrowed:',library[key][3],'|', 'Copies Available:',library[key][4])

def add_book(library, addISBN, addAuthor, addTitle, addStock, addCopiesBorrowed, addCopiesAvailable):
    '''function to add a new book '''
    library[addISBN] = addAuthor, addTitle, addStock, addCopiesBorrowed, addCopiesAvailable
    print("New book added successfully!")


def stock_up(library, addISBN):
    ''' function to update the stock of an existing book '''
    for key in library:
        if key == addISBN:
            copies_update = int(input("Insert the number of new copies to add: "))
            library[addISBN][2] = library[addISBN][2] + copies_update
            library[addISBN][4] = library[addISBN][4] + copies_update
            print("Stock successfully updated!")
            return

def check_out(library, ISBN):
    ''' function to borrow a book '''
    for key in library:
        if key == ISBN:
            copies_borrowed = int(input("Insert the number of copies to borrow: "))
            library[ISBN][4] = library[ISBN][4] - copies_borrowed
            if library[ISBN][4] < 0:
                library[ISBN][4] = library[ISBN][4] + copies_borrowed
                print("The book requested does not have the amount of copies needed to satisfy your request at the moment.")
                return
            else:
                library[ISBN][3] = library[ISBN][3] + copies_borrowed
                print("Operation successfully registered!")
            return


def search_book(library, Title):
    ''' function to search for a book  '''
    for key in library:
        if Title in library[key]:
            print('The ISBN is: ', key)
            break

# Menu and loop to execute each options and to check for invalid entry
print("Welcome to the Coding library!")
menu = {}
menu['1'] = "Search for a book"
menu['2'] = "Print all library details"
menu['3'] = "Add a new book or stock up an existing title"
menu['4'] = "Borrow a book"
print("MENU:")
sorted_options = sorted(menu.keys())
for entry in sorted_options:
    print(entry, menu[entry])
while True:
        selection = input("\nPlease enter an option number or press zero to exit:")
        if selection =='1':
            Title1 = input("Which title are you looking for? ")
            search_book(library1, Title1)
        elif selection == '2':
            print(print_detail(library1))
        elif selection == '3':
            while True:
                addISBN1 = input("Insert ISBN: ")
                if len(addISBN1) < 13:
                    print("ISBN too short")
                    continue
                elif len(addISBN1) > 13:
                    print("ISBN too long")
                    continue
                else:
                    try:
                        addISBN1 = int(addISBN1)
                        if addISBN1 in library1:
                            print('Book already registered.')
                            stock_up(library1, addISBN1)
                            break
                        else:
                            addAuthor1 = input("Insert the full name of the author: ")
                            addTitle1 = input("Insert title: ")
                            addStock1 = int(input("Add the number of copies purchased: "))
                            addCopiesBorrowed1 = 0
                            addCopiesAvailable1 = addStock1
                            add_book(library1, addISBN1, addAuthor1, addTitle1, addStock1, addCopiesBorrowed1, addCopiesAvailable1)
                            break
                    except:
                        print("You cannot use letters for ISBN!")
                        continue
        elif selection == '4':
            ISBN1 = int(input("Insert ISBN to borrow: "))
            if ISBN1 in library1:
                check_out(library1, ISBN1)
            else:
                print("This title is not available in our library")
        elif selection == '0':
            break

        else:
            print("The option you have selected does not exist, please try again.")

