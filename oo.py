"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
Ans: 1. Abstraction: Hiding details we don't need. Abstraction allows only the 
        essential things are displayed to the user. Abstraction is concerned
        with ideas rather than events. It’s like a user running a program (Web
        Browser) without seeing the background codes. Abstraction is achieved
        in either Abstract classes or interface in Python.
     2. Encapsulation: Keeping everything "together". it is bundling of data 
        with the methods that operates on that data. If class is called in ten
        methods then we don't need to update the entire methods rather we 
        updates a single class. Once the class is changed, it automatically
        updates the metods accordingly.
     3. Polymorphism: Interchangeability of components. It means existing in
        many forms. Variables, functions, and objects can exist in 
        multiple forms in Python. There are two types of polymorphism 
        which are run time polymorphism and compile-time polymorphism. Run time
        can take a different form while the application is running and 
        compile-time can take a different form during compilation. The goals of 
        Polymorphism in Object-oriented programming is to enforce simplicity,
        making codes more extendable and easily maintaining applications.
(replace this with your answer)


2. What is a class?
Ans: Classes are a core part of object-oriented programming. Classes can't have 
entirely empty bodies(just like functions and if statement and other block in 
Python). To make instances of the class, we call the class and this process is 
called instantiation.
(replace this with your answer)


3. What is a method?
Ans: A method is like a function defined on a class and method has always at 
least one parameter, self. Method can refer to attributes. So, when you call 
a method, Python passes instance as self.
(replace this with your answer)


4. What is an instance in object orientation?
Ans: An Instance, in object-orientation is a specific realization of any object.
An object may be varied in a number of ways. Each time a program runs, it is an
instance of that program. In languages that create objects from classes, an 
object is an instantiation of a class.


(replace this with your answer)


5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
Ans: There is small diffrence between class attributes and a instance attribute.
The class attribute is a piece of data on the class itsef; when you ask for this
on an instance, its finds it on the class. An instance attribute is set directly
on the object.
This makes a difference if you create a class, object, and then update the 
class.
(replace this with your answer)
"""


"""2. Road Class"""


# Replace this with your code


"""3. Update Password"""


class User:
    """A user object."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username
        self.password = password
    def update_password(self, current_pwd, new_pwd):
        if self.password == current_pwd:
            self.password = new_pwd
    

"""4. Build a Library"""


class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        """Create a book with the given title and author."""

        self.title = title
        self.author = author
        self.is_checked_out = False



class Library(object):
    

    def __init__(self):
        self.library_name = 'Hackbright'
        self.books = []
        self.books.append(Book('Book 1','Author 1'))
        self.books.append(Book('Book 2','Author 2'))
        self.books.append(Book('Book 3','Author 3'))
        self.books.append(Book('Book 4','Author 4'))
        self.books.append(Book('Book 5','Author 5'))

    def get_book(self,name):
        for each in self.books:
            if each.title == name:
                return each

    def check_out(self, book_title):
        book_found = self.get_book(book_title)
        if book_found is not None:
            book_found.is_checked_out = True
        else:
            print('Book not found')

    def check_in(self,book_title):
        book_found = self.et_book(book_title)
        if book_found is not None:
            book_found.is_checked_out = False
        else:
            print('Book does not belong to this library')


    def available_books(self):
        for each in self.books:
            if each.is_checked_out == False:
                print(f"{each.title}")

"""5. Rectangle"""

class Rectangle:
    """A rectangle."""

    def __init__(self, length, width):
        """Create a rectangle with the given length and width."""
        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the area of the rectangle."""
    
        return self.length * self.width
