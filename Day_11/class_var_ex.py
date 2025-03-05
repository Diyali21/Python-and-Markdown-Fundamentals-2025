# Class variable - for all the instance value remains same
# instance variable -> for each instance value is different
class Circle:
    # Class variable
    pi = 3.14

    def __init__(self, radius):
        # instance variable
        self.radius = radius

    def calculate_area(self):
        return Circle.pi * (self.radius**2)


c1 = Circle(2)
c2 = Circle(4)

print(c1.pi)
print(c2.pi)
print(Circle.pi)
