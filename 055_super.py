"""
super() = Function used in a child class to call methods from a parent class (superclass)
        Allows you to extend the functionality of the inherited methods
"""

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    # method overwritign, if child has the same method, then we instance will use this one

    def describe(self):
        print(f"The area of the circle is {3.14 * self.radius *self.radius} cm2")
        super().describe() # extending functionality

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"The area of the square is {self.width * self.width} cm2")
        super().describe() # extending functionality

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"The area of the triangle is {self.height * self.width / 2} cm2")
        super().describe() # extending functionality


circle = Circle(color = "red", is_filled= True, radius = 5)
square = Square(color = "blue", is_filled= False, width = 5)
triangle = Triangle(color = "green", is_filled= True, width = 5, height = 3)

print(square.width)
print(circle.color)
print(triangle.is_filled)

square.describe()
circle.describe()
triangle.describe()