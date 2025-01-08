"""
Polymorphism = Greek word that means to "have many forms or faces"
               Poly = Many
               Morphe = Forms

               2 ways of achiveing polymorphism
               1. Inheritance = An object could be trated of the same type as a parent class
               2. "Duck typing" = Object must have necessary attributes/methods

"""
from abc import abstractmethod, ABC

# absrtract is kinda ike a placeholder, to enforce to any subclass
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


shapes = [Circle(5), Square(5), Triangle(6,7), Pizza("Peporoni", 4)]

for shape in shapes:
    print(f"{shape.area():.2f} cm")


