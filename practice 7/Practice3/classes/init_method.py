#1 Constructor with two parameters
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Aya", 18)
print(p.name, p.age)

#2 Constructor with default value
class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

b = Book("Kazakh Literature")
print(b.title, b.author)

#3 Constructor storing a list
class Classroom:
    def __init__(self, students):
        self.students = students

c = Classroom(["Kanat", "Aruzhan"])
print(c.students)

#4 Constructor with calculation
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14 * radius * radius

circle = Circle(5)