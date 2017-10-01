# Library hardcoded

library1 = {'ISBN':[1234567890123,1234567890124, 1234567890125], 'title':['Intro to Python','Intro to Java','Intro to PHP',],
         'author':['Saverio Pulizzi','John Smith','Mary Land'], 'stock':[3,3,3], 'copies borrowed':[0,0,0], 'copies available':[3,3,3]}

#Function to print all the books details

def print_detail(library):
    for key, value in library.items():
        print(key,':', value)

def add_book(addISBN, addTitle, addAuthor, addStock, addCopiesAvailable, addCopiesBorrowed):

    library1['ISBN'].append(addISBN)
    print('New ISBN addedd successfully!')

    library1['title'].append(addTitle)
    print('New Title addedd successfully!')

    library1['author'].append(addAuthor)
    print('Author addedd successfully!')

    library1['stock'].append(addStock)
    print('Stock addedd successfully!')

    library1['copies available'].append(addCopiesAvailable)

    library1['copies borrowed'].append(addCopiesBorrowed)


def stock_up(library, addISBN):
    for element in library['ISBN']:
        index = library['ISBN'].index(element)
        if element == addISBN:
            copies_update = int(input("Insert the number of new copies to add: "))
            for i in library['stock']:
                library['stock'][index] = library['stock'][index] + copies_update
                for i in library['copies available']:
                    library['copies available'][index] = library['copies available'][index] + copies_update
                    return

def check_out(library, ISBN):
    for element in library['ISBN']:
        index = library['ISBN'].index(element)
        if element == ISBN:
            copies_borrowed = int(input("Insert the number of copies borrowed: "))
            library['copies available'][index] = library['copies available'][index] - copies_borrowed
            if library['copies available'][index] < 0:
                library['copies available'][index] = library['copies available'][index] + copies_borrowed
                print("The book requested does not have the amount of copies that satisfy your request at the moment.\nPlease add below your email address and we will notify you once will be available again.",)
                input("Email Address: ")
                return
            else:
                library['copies borrowed'][index] = library['copies borrowed'][index] + copies_borrowed
                print("Operation successfully registered!")
            return


def search_book(library, Title):
    for element in library['title']:
        index = library['title'].index(element)
        if Title == element:
            print('The ISBN is: ',library['ISBN'][index])

    if Title not in library['title']:
            print("Title does not found")


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
        selection= input("\nPlease enter an option number or press zero to exit:")
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
                        if addISBN1 in library1['ISBN']:
                            print('Book already registered.')
                            stock_up(library1, addISBN1)
                            break
                        else:
                            addTitle1 = input("Insert title: ")
                            addAuthor1 = input("Insert the full name of the author: ")
                            addStock1 = int(input("Add the number of copies purchased: "))
                            addCopiesAvailable1 = addStock1
                            addCopiesBorrowed1 = 0
                            add_book(addISBN1, addTitle1, addAuthor1, addStock1, addCopiesAvailable1, addCopiesBorrowed1)
                            break
                    except:
                        print("You cannot use letters for ISBN!")
                        continue
        elif selection == '4':
            ISBN1 = int(input("Insert ISBN to borrow: "))
            check_out(library1, ISBN1)

        elif selection == '0':
            break

        else:
            print("The option you have selected does not exist, please try again.")

