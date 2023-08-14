class CentralLibrary():
    def __init__(self,book):
        self.book=book
        
    def DisplayBooks(self):
        print("========Book Available in this library are=========")
        for book in self.book:
            print("\t*",book)
    
    def Borrowbook(self):
        item=input("Enter the name of book you  want to borrow:")
        name=input("Enter your name :")
        if item in self.book:
            self.book.remove(item)
            print(f"{item} This book is now issued to your name {name},\n Kindly return it within 30 Days ") 
        else:
            print("Book is currently not available ! Pardon the inconvenience.")    
            
    def ReturnBook(self):
        per=input("Enter Your Name:")
        add=input("Enter The Name of Book You Want to Return/Add:")
        self.book.append(add)
        print("Thank You Mr/Mrs {per} for returning the book {add} , Hope You Enjoyed it reading ! ")
        

if __name__ == '__main__':
    library=CentralLibrary(["Django","Flask","DBMS","Artificial Intelligence","Computer Networks","Web Technology"])
    while(True):
        print("############### WELCOME TO CENTRAL LIBRARY ##################")
        print("Kindly select your option")
        print("\t 1.Display Books \n\t 2.Borrow Book \n\t 3.Return/Add Book \n\t 4.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            library.DisplayBooks()
        elif choice==2:
            library.Borrowbook()
        elif choice==3:
            library.ReturnBook()
        elif choice==4:
            print("Thanks For visiting Central Library! Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice! Choose correct option")
    