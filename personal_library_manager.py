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

menu()