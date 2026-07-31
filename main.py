import json
from config import BOOKS_FILE

library_name = "Welcome to Smart Library Management System (SLMS)"
version = "1.0"

#The book list
books = []


#Function to generate ID
def generate_Id():
    if not books:
        return "BK1001"
    
    highest_id = max(int (book["id"][2:]) for book in books) 

    return f"BK{highest_id + 1}"




#create save book
def save_books():
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)



def load_books():
    global books

    try:
        with open(BOOKS_FILE, "r") as file:
            books = json.load(file)

    except FileNotFoundError:
        books = []


#clear screen
def clear_screen():
    #windows
    import os
    os.system("cls" if os.name == "nt" else "clear")



#create a welcome header
def show_header():
    print("=" * 60)
    print("SMART LIBRARY MANGEMENT SYSTEM")
    print("=" * 60)
    print()

#Build the menu
def show_menu():
    print("1. Book Management")
    print("2. Member Management")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search")
    print("6. Reports")
    print("7. Backup Database")
    print("8. Restore Database")
    print("9. Exit")

#Book Management Menu
def book_management_menu():
    clear_screen()



    def add_book():
        print("ADD NEW BOOK")
        print("-" * 30)

        #ask for input
        book_id = generate_Id()
        title = input("Tiltle: ")
        author = input("Author: ")
        category = input("Category: ")
        year = input("Year: ")
        copies = input("Copies: ")

        book = {
            "id": book_id,
            "title": title,
            "author": author,
            "category": category,
            "year": year,
            "copies": copies,
            "available copies": copies,
            "times borrowed": 0,
        }

        books.append(book)
        save_books()

        print("Book Added Successfully")

   
    def view_books():
        print("\nLIBRARY BOOKS")
        print("-" * 50)

        for book in books:
            print (f"ID: {book['id']}")
            print (f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print(f"Year: {book['year']}")
            print(f"Copies: {book['copies']}")
            print("-" * 50)

        if len(books) == 0:
            print("No books available.")
            return
        

        #JSON is just a text file used to store structured data.

    def edit_books():
        print("\nEdit Book")
   
    def delete_books():
        print("\nDelete Book")


    while True:
        print("\n" + "=" * 40)
        print("BOOK MANAGEMENT")
        print("=" * 40)

        print("1. Add Book")
        print("2. View Books")
        print("3. Edit Book")
        print("4. Delete Book")
        print("5. Back")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            edit_books()

        elif choice == "4":
            delete_books()
           
        elif choice == "5":
            break

        else:
            print("\nInvalid Option.")

        input("\nPress Enter to continue...")


load_books()

#Main Menu Loop
while True:
    clear_screen()
    show_header()
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        book_management_menu()
    elif choice == "2":
        print("Member Management")
    elif choice == "3":
        print("Borrow Book")
    elif choice == "4":
        print("Return Book")
    elif choice == "5":
        print("Search")
    elif choice == "6":
        print("Reports")
    elif choice == "7":
        print("Backup Database")
    elif choice == "8":
        print("Restore Database")
    elif choice == "9":
        print("Thank you for using Smart Library System")
        break
    else:
        print("Invalid Option.")

    print("You selected: ", choice)

    input("Press Enter to continue....")




