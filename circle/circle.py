import math


class Circle():
    def __init__(self, radius) -> None:
        self.radius = self.validate_radius(radius)

    @staticmethod
    def validate_radius(radius):
        if radius == 0:
            raise ValueError("Multiplying with zero should raise a ValueError")
        elif radius < 0:
            raise ValueError("Multiplying with a negative number should raise a ValueError")
        else:
            return radius

    def get_radius(self):
        return self.radius

    def set_radius(self,radius):
        self.radius = self.validate_radius(radius)

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius 

    def __mul__(self, n):
        return Circle(self.radius * n)

    def __str__(self):
        return f"Radius : {self.radius}"