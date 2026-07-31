import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_DIR = os.path.join(BASE_DIR, "database")

BOOKS_FILE = os.path.join(DATABASE_DIR, "books.json")

