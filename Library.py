class Library:

    def __init__(self,nameOfLibrary,listOfBooks) :
       self.name = nameOfLibrary
       self.books = listOfBooks
       self.lend = {}

    def Display_books(self):
        print(f"We have the following books......")
        for i in self.books:
            print(i)
    def lendBook(self,user , book):
        if book not in self.lend.keys():
            self.lend.update({book:user})
            print(f"{user} can take book now")
        else:
            print(f"Book is with {self.lend[book]}")  

    def addBook(self,book):
        self.books.append(book)
        print("Book hasbeen added") 

    def returnBook(self,book):
        self.lend.pop(book)   
        print("Book returned") 
        
if __name__=="__main__" :
    mylib = Library("Golden view Library",["Karam hi Dharam","Rang de basanti","Role of Alertness"])  
    while True:
        print(f"Welcome to {mylib.name} \nEnter your Choices :")        
        print("1. Display all the BOoks ")
        print("2. Add Books ")
        print("3. Lend a Book")
        print("4. Return a Book")
        choice = int(input())
        if(choice==1):
            mylib.Display_books()
        elif(choice==2):
            bk = input("Enter name of the book : ")
            mylib.addBook(bk)
        elif(choice==3):
            user_name = input("Enter your name:")
            bk = input("Enter name of the boook:")
            mylib.lendBook(user_name,bk)    
        elif(choice==4):
            bk = input("Name of the Book:")
            mylib.returnBook(bk)   
        else:
            print("not a valid choice")
        print("Press q to quit or c to continue")
        m = input()
        if m=="c":
            continue
        elif m=="q":
            exit()
        else:
            print("invalid choice , exited......")
            exit()

