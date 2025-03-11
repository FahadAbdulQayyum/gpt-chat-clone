import json
from typing import List, Dict, Any

# Define the type for a single book entry
Book = Dict[str, Any]
Library = dict[
    "book_title": str,
    "book_author": str,
    "publication_year": str,
    "genre": str,
    "read_this_book": str,
]

def menu() -> None:
    choice: str = str(input(
    """
    Welcome to your Personal Library Manager!  
    1. Add a book  
    2. Remove a book  
    3. Search for a book  
    4. Display all books  
    5. Display statistics  
    6. Exit  

    Enter your choice: """
    ))
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
            display_statics()
        case "6":
            print("Library saved to file. Goodbye!")
            exit()
        case _:
            print("Invalid choice. Please try again.")
            menu()
    

def add_a_book() -> None:
    book_title: str = str(input("Enter the book title: "))
    book_author: str = str(input("Enter the author: "))
    publication_year: str = str(input("Enter the publication year: "))
    genre: str = str(input("Enter the genre: "))
    read_this_book: str = str(input("Have you read this book? (yes/no): "))
    print(book_title, book_author, publication_year, genre, read_this_book)
    new_book: dict[str, str] = {
        "title": book_title,
        "author": book_author,
        "publication_year": publication_year,
        "genre": genre,
        "read_this_book": read_this_book}
    library: List[Book] = load_library()

    library.append(new_book)  # Append the new book to the list

    # Step 3: Save the updated library data back to the file
    save_library(library)

def load_library() -> List[Book]:
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


# Function to save the library data to the file
def save_library(library_data: Library):
    with open("library.txt", "w") as file:
        json.dump(library_data, file, indent=4)  # Write the data as a JSON array with indentation


def remove_a_book() -> None:
    title_of_book: str = str(input("Enter the title of the book to remove: "))
    print(title_of_book)

def search_for_a_book() -> None:
    search_by: str = str(input("""
    Search by:  
    1. Title  
    2. Author
                               
    Enter your choice: """))
    print(search_by)

    match search_by:
        case "1":
            title_of_book: str = str(input("Enter the title of the book: "))
            search_by_title(title_of_book)
        case "2":
            author_of_book: str = str(input("Enter the author of the book: "))
            search_by_author(author_of_book)
        case _:
            print("Invalid choice. Please try again.")
            search_for_a_book()

def search_by_title(title: str) -> None:
    print("Search by title", title)

def search_by_author(author: str) -> None:
    print("Search by author", author)

def display_all_books() -> None:
    with open("library.txt", "r") as file:
        content = file.read()
        content_list = list(content.split("\n"))
        print(content_list[0])
        # for book in content_list:
        #     print(book)

def display_statics() -> None:
    print("Display statics")

menu()