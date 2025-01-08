"""
Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
                They are automatically called by many of Pythons built in operations
                They allow developers to define or customize the behaviour of objetcs
"""

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # without this, when printing, it will only give memory allocations. this str method
    # return a string representation
    def __str__(self):
        return f"{self.title} by {self.author}"

    # to compare if 2 objects are the equal
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"key {key} is not found"

book1 = Book('The hobbit', "Tolkien", 310)
book2 = Book("Harry potter", "jk", 223 )
book3 = Book("Narnia", "cs lewis", 172)
book4 = Book("Narnia", "cs lewis", 172)


print(book1)
print(book2)
print(book3)

print(book3 == book2)
print(book3 == book4)
print(book3 < book4)
print(book1 < book2)
print(book1 > book2)

print(book1 + book2)

print("Harry" in book1)
print("Harry" in book2)
print("lewis" in book3)

print(book3["title"])
print(book3["author"])
print(book3["num_pages"])
print(book3["nums"])
