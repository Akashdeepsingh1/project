'''
__str__ - this display data in human consumable format
__rept__ - this display data in program consumable format. - this is internally called by __str__ method.

if these are not implement then - when you print an object or inspect an object then a class name is provided + memory
location.
'''

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return 'a {} color with {} miles'.format(self.color,self.mileage)


car1 = Car('Red', 12345)
car2 = Car('White', 23456)

print(car1)
print(car2)

