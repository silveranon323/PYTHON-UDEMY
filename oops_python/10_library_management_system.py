class Library:
    def __init__(self,listOfBooks):
        self.available_books=listOfBooks
    def display_available_books(self):
        print()
        print("Available Books")
        for book in self.available_books:
            print(book)
        
    def lend_books(self,requested_book):
        if requested_book in self.available_books:
            print("You have now borrowed the book")
            self.available_books.remove(requested_book)
        else:
            print("Sorry the book is not available in our list.")

        
    def addBook(self,returned_book):
        self.available_books.append(returned_book)
        print("You have returned the books thank you.")
class Customer:
    def request_books(self):
        print("Enter the name of the book you would like to borrow: ")
        self.book=input()
        return self.book
        
    def return_book(self):
        print("Which book are you returning:")
        self.book=input()
        return self.book       
library=Library(["Think and grow reach.","Who will cry when you will die.","For one more day."])
customer=Customer()

print("Enter 1 to display the available books.")
print("Enter 2 to request for a book.")
print("Enter 3 to return the available books.")
print("Enter 4 to exit.")
user_choice=int(input("Enter your choice."))
match user_choice:
    case 1:
        library.display_available_books()
    case 2:
       requested_book=customer.request_books()
       library.lend_books(requested_book)
    case 3:
        return_book=customer.return_book()
        library.addBook(return_book)
    case 4:
        exit
    case _ :
        print("Invalid input")