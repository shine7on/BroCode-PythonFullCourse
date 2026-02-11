# Magic Methods (__init__, __str__, __eq__)
# dunder methods: double underscore
# automatically called by many of Pythons built-in operation


class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        if self.title == other.title and self.author == other.author:
            return True
        return False
    
    def __lt__(self, other):
        if self.num_pages < other.num_pages:
            return True
        return False
    
    def __gt__(self,other):
        return self.num_pages > other.num_pages
    
    def __add__(self,other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title
    
    def __getitem__(self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.pages
        else:
            return f"Key {key} was not found"
        
    



book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 310)


print(book1)
print(book3)
print(book1 == book4)
print(book1 > book2)
print(book1 < book3)
print(book1 + book4)

print("Hobbit" in book1)
print("Hobbit" in book3)

print(book1["title"])
print(book2["author"])
print(book1["key"])
