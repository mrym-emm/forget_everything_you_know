""""
object = A "bundle" of related attributes (variables) and methods (functions)
        EX. phone, cup, book
        You need a "class" to create many objects

class = (blueprint) used to design the structure and layout of an object
"""

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.model} {self.year} {self.color}")
        if self.for_sale == True:
            print('This car is for sale')
        else:
            print('This car is NOT for sale')



car_1 = Car(model = "Toyota", year = 1999, color = "red", for_sale = True)
car_2 = Car(model = "Honda", year = 2004, color = "blue", for_sale = False)
car_3 = Car(model = "Ford", year = 1972, color = "green", for_sale = True)


print(car_1.model)
print(car_1.year)
print(car_1.color)
print(car_1.for_sale)

car_3.stop()
car_2.stop()

car_2.drive()
car_1.drive()

car_1.describe()
car_2.describe()
car_3.describe()