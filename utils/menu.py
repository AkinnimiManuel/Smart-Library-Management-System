from utils.helper import *
from services.book_service import *

library_name = "Welcome to Smart Library Management System (SLMS)"
version = "1.0"

#create a welcome header
def show_header():
    print("=" * 60)
    print(f"{library_name} - Version {version}")
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