# Menu-driven CRUD operations on an in-memory list of books.
books = [{"id": 1, "title": "Python Basics", "author": "A. Kumar"}]
while True:
    print("\n1 Add  2 View  3 Update  4 Delete  5 Exit")
    choice = input("Choose: ").strip()
    try:
        if choice == "1":
            book_id = max((book["id"] for book in books), default=0) + 1
            books.append({"id": book_id, "title": input("Title: ").strip(), "author": input("Author: ").strip()})
            print("Book added with ID", book_id)
        elif choice == "2":
            print(*books, sep="\n") if books else print("No books.")
        elif choice == "3":
            book_id = int(input("Book ID: "))
            book = next((item for item in books if item["id"] == book_id), None)
            if book:
                book["title"] = input("New title: ").strip()
                book["author"] = input("New author: ").strip()
                print("Book updated.")
            else:
                print("Book not found.")
        elif choice == "4":
            book_id = int(input("Book ID: "))
            old_count = len(books)
            books[:] = [book for book in books if book["id"] != book_id]
            print("Book deleted." if len(books) < old_count else "Book not found.")
        elif choice == "5":
            break
        else:
            print("Choose an option from 1 to 5.")
    except ValueError:
        print("Book ID must be a number.")
