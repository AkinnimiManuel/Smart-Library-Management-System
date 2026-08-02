import json
from config import BOOKS_FILE
from services.storage_service import *
from services.book_service import *

library_name = "Welcome to Smart Library Management System (SLMS)"
version = "1.0"

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


load_data(BOOKS_FILE)  # Load books from the JSON file at the start of the program

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




