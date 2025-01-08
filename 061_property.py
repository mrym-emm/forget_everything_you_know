"""
@property = Decorator used to define a method as a property (it can be accessed like an attribute)
            Benefit: Add additional logic when read, write or delete attributes
            Gives you getter(defalt propety), setter and deleter method
"""

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height


    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        return f"{self._height:.1f} cm"

    @width.setter
    def width(self, new_width):
        # remember _ means private here
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        # remember _ means private here
        if new_height > 0:
            self._width = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")


rectangle = Rectangle(3,4)

# this is technically private
print(rectangle._width)
print(rectangle._height)

rectangle.height = -2
rectangle.width = 0
rectangle.width = 1

del rectangle.width
del rectangle.height

# # this is technically private
# print(rectangle.width)
# print(rectangle.height)