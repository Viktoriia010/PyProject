from Book import Book

def create_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")

    if not title or not author:
        print("Title and author cannot be empty.")
        return None

    try:
        year = int(input("Enter publication year: "))
        pages = int(input("Enter number of pages: "))

        return Book(title, author, year, pages)

    except ValueError as error:
        print("Invalid data:", error)
        return None

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("It`s not a Book")
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book «{title}» deleted successfully.")
                return

        print("Book not found.")

    def sort_books(self):
        self.books.sort()
        self.print_books()

    def print_books(self):
        if len(self.books)==0:
            print("No books available")
            return
        for book in self.books:
            print(book)

    def search_book(self, keyword):
        results = []

        for book in self.books:
            if (keyword.lower() in book.title.lower()
                    or keyword.lower() in book.author.lower()):
                results.append(book)

        if results:
            for book in results:
                print(book)
        else:
            print("No books found.")

    def __len__(self):
        return len(self.books)

    def __bool__(self):
        return bool(self.books)


library = Library()

while True:
    print("""
    1 - Add a book
    2 - Remove a book
    3 - Display all books
    4 - Search for a book
    5 - Sort books by page count
    6 - Number of books
    7 - Compare two books
    8 - Calculate total pages of two books
    0 - Exit
    """)

    choice = input("Choose an option: ")

    if choice == "1":
        book = create_book()
        if book is not None:
            library.add_book(book)

    elif choice == "2":
        title = input("Enter a book title for deletion: ")
        library.remove_book(title)

    elif choice == "3":
        library.print_books()

    elif choice == "4":
        keyword = input("Enter a book title or a book author: ")
        library.search_book(keyword)

    elif choice == "5":
        library.sort_books()

    elif choice == "6":
        print("Book counts:", len(library))
        print("Library not empty:", bool(library))


    elif choice == "7":
        if len(library.books) < 2:
            print("Add at least 2 books.")
            continue

        library.print_books()
        try:
            i = int(input("Enter the number of the first book: ")) - 1
            j = int(input("Enter the number of the second book: ")) - 1

            book1 = library.books[i]
            book2 = library.books[j]

            print("Books have the same title and author:", book1 == book2)
            print("First book has fewer pages:", book1 < book2)
            print("First book has more pages:", book2 < book1)

        except (ValueError, IndexError):
            print("Invalid book number.")

    elif choice == "8":
        if len(library.books) < 2:
            print("Add at least 2 books.")
            continue

        library.print_books()
        try:
            i = int(input("Enter the number of the first book: ")) - 1
            j = int(input("Enter the number of the second book: ")) - 1

            print("Total number of pages:", library.books[i] + library.books[j])

        except (ValueError, IndexError):
            print("Invalid book number.")

    elif choice == "0":
        break

    else:
        print("Unknown option.")


