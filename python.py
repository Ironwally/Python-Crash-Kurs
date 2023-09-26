"""a = int(input("Gimme Numbers: "))
b = int(input("Gimme more numbers: "))
print("Numba is: ", a+b)


for i in range(6):
    print(i)


#aufgabe 2
import random
s = random.randint(0,9)

things = []
inp = s+1
tries = 0
while s != inp:
    inp = (int(input("Gimme Numba like s! ")))
    things.append(inp)
    tries += 1
print(tries)
print(things)
"""

#Aufgabe 3

class Book:
    def __init__(self, title, weight):
        self.title = title
        self.weight = weight
    
one = Book("One Piece", "5 Kilo")
two = Book("Two Piece", "10 Kilo")
three = Book("Three Piece", "15 Kilo")

class Library:
    def __init__(self):
        self.books = []    
    def add_book(self, book):
        self.books.append(book)

lib = Library()
lib.add_book(one)

print(*lib.books, sep = ", ")


