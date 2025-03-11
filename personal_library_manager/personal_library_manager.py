import json
from typing import List, Dict

# Define the type for a single book entry
Book = Dict[str, str]

# Define the type for the library (a list of books)
Library = List[Book]

def menu() -> None:
    choice: str = input(
    """
    Welcome to your Personal Library Manager!  
    1. Add a book  
    2. Remove a book  
    3. Search for a book  
    4. Display all books  
    5. Display statistics  
    6. Exit  

    Enter your choice: """
    )
    match choice:
        case "1":
            add_a_book()
        case "2":
            remove_a_book()
        case "3":
            search_for_a_book()
        case "4":
            display_all_books()
        case "5":
            display_statistics()
        case "6":
            print("Library saved to file. Goodbye!")
            exit()
        case _:
            print("Invalid choice. Please try again.")
            menu()

def add_a_book() -> None:
    book_title: str = input("Enter the book title: ")
    book_author: str = input("Enter the author: ")
    publication_year: str = input("Enter the publication year: ")
    genre: str = input("Enter the genre: ")
    read_this_book: str = input("Have you read this book? (yes/no): ")

    # Create a new book dictionary
    new_book: Book = {
        "book_title": book_title,
        "book_author": book_author,
        "publication_year": publication_year,
        "genre": genre,
        "read_this_book": read_this_book  # Convert to boolean
    }

    # Load the existing library
    library: Library = load_library()

    # Append the new book to the library
    library.append(new_book)

    # Save the updated library back to the file
    save_library(library)

    print(f"Book '{book_title}' added successfully!")

def load_library() -> Library:
    try:
        # Open the file in read mode
        with open("library.txt", "r") as file:
            content = file.read()
            if content.strip():  # Check if the file has non-whitespace content
                return json.loads(content)  # Parse the JSON content into a Python list
            else:
                return []  # Return an empty list if the file is empty
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist

def save_library(library_data: Library) -> None:
    with open("library.txt", "w") as file:
        json.dump(library_data, file, indent=4)  # Write the data as a JSON array with indentation

def remove_a_book() -> None:
    title_of_book: str = input("Enter the title of the book to remove: ")

    # Load the existing library
    library: Library = load_library()

    # Find and remove the book with the matching title
    updated_library = [book for book in library if book["book_title"].lower() != title_of_book.lower()]

    if len(updated_library) < len(library):
        # Save the updated library back to the file
        save_library(updated_library)
        print(f"Book '{title_of_book}' removed successfully!")
    else:
        print(f"Book '{title_of_book}' not found.")

def search_for_a_book() -> None:
    search_by: str = input("""
    Search by:  
    1. Title  
    2. Author
                               
    Enter your choice: """)
    match search_by:
        case "1":
            title_of_book: str = input("Enter the title of the book: ")
            search_by_title(title_of_book)
        case "2":
            author_of_book: str = input("Enter the author of the book: ")
            search_by_author(author_of_book)
        case _:
            print("Invalid choice. Please try again.")
            search_for_a_book()

def search_by_title(title: str) -> None:
    library: Library = load_library()
    matches = [book for book in library if title.lower() in book["book_title"].lower()]
    if matches:
        print(f"Found {len(matches)} book(s) with title containing '{title}':")
        for book in matches:
            print(book)
    else:
        print(f"No books found with title containing '{title}'.")

def search_by_author(author: str) -> None:
    library: Library = load_library()
    matches = [book for book in library if author.lower() in book["book_author"].lower()]
    if matches:
        print(f"Found {len(matches)} book(s) by author containing '{author}':")
        for book in matches:
            print(book)
    else:
        print(f"No books found by author containing '{author}'.")

def display_all_books() -> None:
    library: Library = load_library()
    if library:
        print("All Books:")
        for book in library:
            print(book)
    else:
        print("No books in the library.")

def display_statistics() -> None:
    library: Library = load_library()
    total_books = len(library)
    read_books = sum(1 for book in library if book["read_this_book"])
    percentage_read = (read_books / total_books) * 100

    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read}%")

menu()