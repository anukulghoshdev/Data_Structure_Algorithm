# Encapsulation
# Inheritance 
# Polymorphism
# Abstraction



# Class definition
class Car:
    # Class attribute (সব objects এর জন্য common) / # Class property
    wheels = 4
    
    # Constructor method (object তৈরি হলে automatically call হয়)
    def __init__(self, brand, model, year):
        # Instance attributes (প্রতিটি object এর নিজস্ব) / # Instance property
        self.brand = brand
        self.model = model
        self.year = year
    
    # Instance method
    def display_info(self):
        return f"{self.brand} {self.model} ({self.year})"
    
    # Class method
    @classmethod
    def change_wheels(cls, new_count):
        cls.wheels = new_count
    
    # Static method (self বা cls receive করে না)
    @staticmethod
    def is_vintage(year):
        return year < 1990

# Object creation
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2018)

print(car1.display_info())  # Toyota Corolla (2020)
print(car2.display_info())  # Honda Civic (2018)
print(Car.wheels)          # 4





class Node: 
    x = 4
    def __init__(): 
        pass
###
class Person:
    species = "Human" 
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def greet(self):
        pass
        # print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


p1 = Person("Alice", 30)

p1.greet()  # Hello, my name is Alice and I am 30 years old.
p1.display_info()

print(p1.name)  
print(p1.age)   


class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."
calc = Calculator()
print(calc.add(3, 5))        # 15
print(calc.subtract(10, 4))  # 6
print(calc.multiply(2, 6))   # 12   
print(calc.divide(46, 2))     # 4.0
print(calc.divide(4, 0))     # Error! Division by zero.
print(calc.divide(0, 4))     # 0.0

class Playlist:
    def __init__(self):
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
    
    def display_songs(self):
        for song in self.songs:
            print(f"- {song}")

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Dustu Kokil")
my_playlist.add_song("Ay Ay chad mama")
my_playlist.add_song("Lage Ora Dhura")
my_playlist.show_songs()