from config import BOOKS_FILE
from services.storage_service import *

# Load books when this module is imported
books = load_data(BOOKS_FILE)

#Function to generate ID
def generate_Id():
    if not books:
        return "BK1001"
    
    highest_id = max(int (book["id"][2:]) for book in books) 

    return f"BK{highest_id + 1}"


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
        save_data(BOOKS_FILE, books)

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