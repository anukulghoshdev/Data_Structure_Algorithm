# Encapsulation
# Inheritance 
# Polymorphism
# Abstraction



# Class definition
class Car:
    # Class attribute (সব objects এর জন্য common)
    wheels = 4
    
    # Constructor method (object তৈরি হলে automatically call হয়)
    def __init__(self, brand, model, year):
        # Instance attributes (প্রতিটি object এর নিজস্ব)
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