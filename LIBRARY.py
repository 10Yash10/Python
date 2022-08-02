class Library():
    books = ['python','c','c++','html','css','java','java script']
    def add_book(self,name):
        self.books.append(name)
        
    def remove_book(self,name):
        if name in self.books:
            self.books.remove(name)
        else:
            print(name)
            print(f"{name} Book has already been issued")

    def show_book(self,):
        if self.books != []:
            for i in self.books:
                print(i)
        else:
            print("All the books have been issued.Please wait until the reader returns the books.")
# class User():
#     pass
#     def show_users(self):
#         pass

user = Library()      
while(True):
    print()
    print("****************************************************************")
    print("             Press 1 to add a book")
    print("             Press 2 to issue a book")
    print("             Press 3 to show the books present in the library")
    print("             Press 4 to exit the library")
    print("****************************************************************")
    print()
    choice = int(input("Enter your choice: "))
    print()
    try:
        if choice == 1:
            book_name = input("Enter the book you want to add:")
            user.add_book(book_name)

        elif choice == 2:
            issue_book = input("Enter the book you want to issue: ")
            user.remove_book(issue_book)
            print(f"{issue_book} book has been issued.")

        elif choice == 3:
            user.show_book()

        elif choice == 4:
            break

        else:
            print("You have to select from above choices")
    except Exception as e:
        print(e)
             