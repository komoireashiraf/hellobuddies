##defining the class book
class Book:
    def __init__(self, title, author, year):
       self.title = title
       self.author = author
       self.year = year

    def describe(self):
        return f"{self.title} by {self.author} in {self.year}."

##the books
book1 = Book("Twilight Book 1", "Stephenie Meyer", 2005)
book2 = Book("The Fault in our Stars", "John Green", 2012)

##calling the books
print(book1.describe())
print(book2.describe())
