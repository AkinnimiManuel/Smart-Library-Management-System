from config import BOOKS_FILE
from services.storage_service import *
from services.book_service import *
from utils.helper import *
from utils.menu import *

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




