import json

class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def book_info(self):
        return f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Available: {'Yes' if self.available is True else 'No'}"
    
    def to_dic(self):
        dic = {"book_id": self.book_id,"title": self.title, "author": self.author, "available": self.available,}
        return dic
    
    @classmethod
    def to_object(cls, dic):
        return Book(dic["book_id"], dic["title"], dic["author"], dic["available"])
    
class Member:
    def __init__(self, member_id, name, borrowed_books=None):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = [] if borrowed_books is None else borrowed_books

    def member_info(self):
        return f"Member: {self.name} (ID: {self.member_id}) | Borrowed: {len(self.borrowed_books)} books"
    
    def to_dic(self):
        dic = {"member_id": self.member_id, "name": self.name, "borrowed_books": self.borrowed_books,}
        return dic

    @classmethod
    def to_object(cls, dic):
        return Member(dic["member_id"], dic["name"], dic["borrowed_books"])
    
class Library:
    def __init__(self, books = None, members = None):
        self.books = [] if books is None else books
        self.members = [] if members is None else members

    def add_book(self, book):
        self.books.append(book)
        return f"Book added: {book.title} (ID: {book.book_id})"
    
    def add_member(self, member):
        self.members.append(member)
        return f"Member added: {member.name} (ID: {member.member_id})"
    
    def search_book_by_title(self, title):
        for book in self.books:
            if title.lower() == book.title.lower():
                return book
            
        return None
    
    def list_all_books(self):
        if not self.books:
            print("No books in library.")
        else:
            print("--- All Books ---")
            for book in self.books:
                print(book.book_info())

    def list_all_members(self):
        if not self.members:
            print("No members yet.")
        else:
            print("--- All Members ---")
            for member in self.members:
                print(member.member_info())

    def find_book(self, book_id):
        for book in self.books:
            if book_id == book.book_id:
                return book
        return None
    
    def find_member(self, member_id):
        for member in self.members:
            if member_id == member.member_id:
                return member
        return None
        
    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        if not member:
            return "Member ID not found"
        book = self.find_book(book_id)
        if not book:
            return "Book ID not found"
        if not book.available:
            return "Book not available"
        book.available = False

        member.borrowed_books.append(book.book_id)
        return f"Loan successful: {member.name} borrowed \"{book.title}\""
    
    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        if not member:
            return "Member ID not found"
        book = self.find_book(book_id)
        if not book:
            return "Book ID not found"
        if book_id not in member.borrowed_books:
            return "This member did not borrow this book"
        book.available = True

        member.borrowed_books.remove(book.book_id)
        return f"Return successful: {member.name} returned \"{book.title}\""

    def list_borrowed_books(self):
        print("--- Borrowed Books ---")
        found_any = False
        for member in self.members:
            if not member.borrowed_books:
                pass
            else:
                for book_id in member.borrowed_books:
                    book = self.find_book(book_id)
                    if book is None:
                        print(f"Unknown book ID {book_id} (borrowed by {member.name})")
                        found_any = True
                        continue
                    print(f"{book.title} (borrowed by {member.name})")
                    found_any = True

        if not found_any:
            print("No borrowed books.")

    def load_from_file(self, filename="library.json"):
        try:
            books = []
            members = []
            with open(filename, "r") as file:
                dic = json.load(file)
                dic_books = dic.get("books", [])
                dic_members = dic.get("members", [])
                for item in dic_books:
                    books.append(Book.to_object(item))
                for item in dic_members:
                    members.append(Member.to_object(item))
                self.books = books
                self.members = members
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []
            self.members = []

    def save_to_file(self, filename="library.json"):
        dic = {"books":[], "members":[],}
        for book in self.books:
            dic["books"].append(book.to_dic())
        for member in self.members:
            dic["members"].append(member.to_dic())
        
        with open(filename, "w") as f:
            json.dump(dic, f, indent=2)

def main():
    library = Library()
    library.load_from_file()

    while True:
        print("""
--- Library Menu ---
1) Add book
2) Add member
3) Borrow book
4) Return book
5) List all books
6) List all members
7) List borrowed books
8) Save and Exit
--------------------
""")
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Enter a number between 1 and 8.")
            continue

        if choice not in range(1,9):
            print("Invalid option.")
            continue

        if choice == 8:
            library.save_to_file()
            print("Library saved. Goodbye!")
            break

        if choice == 5:
            library.list_all_books()
            continue

        if choice == 6:
            library.list_all_members()
            continue

        if choice == 7:
            library.list_borrowed_books()
            continue
        
        if choice == 1:
            book_id = input("Enter the book ID: ").strip()
            if library.find_book(book_id) is not None:
                print(f"Book ID: '{book_id}' already exists.")
                continue
            title = input("Enter the book's title: ")
            author = input("Enter the book's author: ")

            book = Book(book_id, title, author)
            print(library.add_book(book))

            continue

        if choice == 2:
            member_id = input("Enter member ID: ").strip()
            if library.find_member(member_id) is not None:
                print(f"The member with '{member_id}' already exists.")
                continue
            name = input("Enter member name: ").strip()

            member = Member(member_id, name)
            print(library.add_member(member))

            continue

        if choice == 3:
            member_id = input("Enter member ID: ").strip()
            book_id = input("Enter book ID: ").strip()
            print(library.borrow_book(member_id,book_id))
            continue

        if choice == 4:
            member_id = input("Enter member ID: ").strip()
            book_id = input("Enter book ID: ").strip()
            print(library.return_book(member_id,book_id))
            continue

if __name__ == "__main__":
    main()