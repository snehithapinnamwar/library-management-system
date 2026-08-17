import os 
from  datetime import datetime
BOOK_FILE = "books.txt"
STUDENT_FILE = "students.txt"
ISSUE_FILE = "issued_books.txt"
class Library:
    def add_book(self):
        print("________add book_______")
        book_id=input("enter book id : ")
        name=input("enter book name: ")
        author=input("enter author name: ")
        qty=input("enter quantity: ")
        with open(BOOK_FILE,"a") as file:
            file.write(f"{book_id},{name},{author},{qty}\n")
        print("book added successfully")
    def view_books(self):
        print("________book list_______")
        if not os.path.exists(BOOK_FILE):
            print("no books available")
            return
        with open(BOOK_FILE,"r") as file:
            books=file.readlines()
            if len(books)==0:
              print("no books found")
              return
            for book in books:
               data=book.strip().split(",")
               print(f"book id:{data[0]}")
               print(f"book name:{data[1]}")
               print(f"book author:{data[2]}")
    def search_book(self):
        print("__________search book__________")                
        search=input("enter book id : ")
        found=False
        with open(BOOK_FILE,"r") as file:
            books=file.readlines()
        for book in books:
            data=book.strip().split(",")
            if search==data[0]:
                found=True
                print(f"book id:{data[0]}")
                print(f"book name:{data[1]}")
                print(f"book author:{data[2]}")
        if not found:
            print("book not  found")
    def delete_book(self):
        print("_______delete book___________")
        delete_id=input("enter book id : ")
        books=[]
        found=False
        with open(BOOK_FILE,"r") as file:
            books_r=file.readlines()
            for book in books_r:
              data=book.strip().split(",")
              if delete_id!=data[0]:
                books.append(book)
              else:
                found=True
        with open(BOOK_FILE,"w") as file:
            file.writelines(books)
        if found:
            print("deleted successfully")
        else:
            print("not found")

    def update_book(self):
        print("____________update book_____________")
        update_id=input("enter id: ")
        books=[]
        with open(BOOK_FILE,"r") as file:
            books_r=file.readlines()
            for book in books_r:
              data=book.strip().split(",")
              if update_id==data[0]:
                  found=True
                  print("enter book details:")
                  name=input("enter book name: ")
                  author=input("enter author name: ")
                  qty=input("enter quantity: ")
                  books.append(f"{update_id},{name},{author},{qty}\n")
              else:
                  books.append(book)
        with open(BOOK_FILE,"w") as file:
            file.writelines(books)
        if found:
            print("updated success")
        else:
            print("not found")
    def add_student(self):
        print("_______________add student____________")
        sid=input("enter student id:")
        sname=input("enter student name:")
        with open(STUDENT_FILE,"a") as file:
            file.write(f"{sid},{sname}\n")
        print("student added successfully")
    def issue_book(self):
        print("__________issue book____________")
        book_id=input("enter  book id:")
        sid=input("enter student id:")
        books=[]
        found=False
        with open(BOOK_FILE,"r") as file:
           books_r=file.readlines()
           for book in books_r:
               data=book.strip().split(",")
               print(type(data[0]),data[0],data[0]==book_id)
               if data[0]==book_id:
                   found=True
                   qty=int(data[3])
                   if qty>0:
                       qty=qty-1
                       print("book issued succesfully")
                       issue_date=datetime.now().strftime("%d-%m-%Y")
                       with open(ISSUE_FILE,"a") as file:
                         file.write(f"{book_id},{sid},{issue_date}\n")
                   else:
                       print("book out of stockkkk")
                   books.append(f"{data[0]},{data[1]},{data[2]},{qty}\n") 
               else:
                    books.append(book)
        with open(BOOK_FILE,"w") as file:
            file.writelines(books) 
        if not found:
            print("book not found")       
    def return_book(self):
        print("__________return book__________")
        book_id=input("enter book id: ")
        records=[]
        found=False
        with open(ISSUE_FILE,"r") as file:
            books=file.readlines()
            for book in books:
               data=book.strip().split(",")
               if book_id!=data[0]:
                    records.append(book)
               else:
                 found=True
                 issue_date=datetime.strptime(data[2],"%d-%m-%Y")
                 return_date=datetime.now()
                 days=(return_date-issue_date).days
                 fine=0
                 if days>7:
                     fine=(days-7)*5        
                     print("return delayed: ",days)            
                     print("fine amount:",fine)
        with open(ISSUE_FILE,"w") as file:
            file.writelines(records)       
        if found:
            books=[]
            with open(BOOK_FILE,"r")as file:
                books_r=file.readlines()
                for book in books_r:
                    data=book.strip().split(',')
                    if data[0]==book_id:
                        qty=int(data[3])
                        qty=qty+1
                        books.append(f"{data[0]},{data[1]},{data[2]},{qty}\n")
                    else:
                        books.append(book)
            with open(BOOK_FILE,"w") as file:
                file.writelines(books)       
            print("book returned successfullyy")
        else:
            print(" issue record not found")
def login():
    user_name="admin"
    password="1"
    user=input("enter username:")
    pwd=input("enter password:")
    if user_name==user and password==pwd:
        print("login successfullyyy")
        return True
    else:
        print("invalid credentials")
        return False
library=Library()
if login():
    while True:
        print('''  
              ...................library management system
              1:Add book
              2:view books
              3:search book
              4:update book
              5:delete book
              6:add student
              7:issue book
              8:return book
              9:exit........................
              ''')
        choice=int(input("enter your choice: "))
        if choice==1:
            library.add_book()
        elif choice==2:
            library.view_books()
        elif choice==3:
            library.search_book()
        elif choice==4:
            library.update_book()
        elif choice==5:
            library.delete_book()
        elif choice==6:
            library.add_student()
        elif choice==7:
            library.issue_book()
        elif choice==8:
            library.return_book()
        elif choice==9:
            print("thanksssss")
            break
        else:
            print("invalid choice")
            
        