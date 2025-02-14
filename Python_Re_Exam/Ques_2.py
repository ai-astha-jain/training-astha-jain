class LibraryManagement:
    def __init__(self):
        self.dictionary = {}
        
    def add_new_books(self):
        while True:
            try:
                no_of_books = int(input("Enter the number of books: "))
            except ValueError:
                print("Please enter the valid integer")
                return True
            for i in range(no_of_books):
                book_name = input("Enter the book name: ")
                if not book_name.isdigit():
                    self.dictionary[book_name] = {}
                else:
                    print("Please enter the valid input")
                    return True
                author_name = str(input("Enter the author name: "))
                self.dictionary[book_name][author_name] = {}
                title_name = str(input("Enter the title of the book: "))
                self.dictionary[book_name][author_name][title_name]={}
                status = "available"
                self.dictionary[book_name][author_name][title_name] = status
            break                  
    
    def check_out_book(self,book_name,author_name,title_name):
        if book_name in self.dictionary:
            if author_name in self.dictionary[book_name]:
                if title_name in self.dictionary[book_name][author_name]:
                    status = "unavailable"
                    self.dictionary[book_name][author_name][title_name] = status
                else:
                    print("No status of book.")
            else:
                print(f"No author found")
        else:
            print(f"Book not found.")
                    
    def display(self):
        print("\n--- Library Management ---")
        for books, authors in self.dictionary.items():
            print(f"\nBook: {books}")
            for author, t in authors.items():
                print(f"\tAuthor: {author}")
            for title,status in t.items():
                print(f"\tTitle: {title}")
                print(f"\tStatus: {status}")
                
                
        
    def menu(self):
        while True:
            print('''
                1. Add new books to the library.
                2. Check out books (mark them as unavailable).
                3. Search for books by title or author.
                4. List available books.
                5. Return a book (mark it as available again). 
                6. Display information about a particular book.
            ''')
        
            choice = input("Enter the choice(0-6): ")
            if choice.isdigit():
                choice = int(choice)
            else:
                print("Invalid choice. Please enter the valid choice")
        
            if choice == 1:
                self.add_new_books()
                self.display()
            elif choice == 2:
                book_name = input("Enter the book name you want to checkout:")
                author_name = input("Enter the author name:")
                title_name = input("Enter the title of book:")
                self.check_out_book(book_name,author_name,title_name)
                self.display()
            elif choice == 6:
                self.display()    
            else:
                break      


output = LibraryManagement()
output.menu()
