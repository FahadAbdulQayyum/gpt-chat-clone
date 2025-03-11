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
    library: dict[str, str] = {
        "title": book_title,
        "author": book_author,
        "publication_year": publication_year,
        "genre": genre,
        "read_this_book": read_this_book}
    
    # Step 1: Check if the file exists and contains data
    try:
        # Open the file in read mode to check its content
        with open("library.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        # If the file does not exist, initialize content as empty
        content = ""

    # Step 2: Decide whether to append or overwrite
    if content.strip():  # Check if the file has non-whitespace content
        # Append the new data to the existing content
        with open("library.txt", "a") as file:
            file.write("\n" + str(library))  # Add a newline before appending
    else:
        # Write the new data directly (file is empty or does not exist)
        with open("library.txt", "w") as file:
            file.write(str(library))

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
    print("Display all books")

def display_statics() -> None:
    print("Display statics")

menu()