import math

class circle1:
    def __init__(self):
        # Prompt the user for the radius input
        self.radius = float(input("Enter the radius of the circle:\n"))

    def area(self):
        Circle_area = math.pi * self.radius**2
        print(f"Area of the circle with radius {self.radius}:\n {Circle_area:.2f}")

    def perimeter(self):
        circle_perimeter = 2 * math.pi * self.radius
        print(f"Perimeter of the circle with radius {self.radius}:\n {circle_perimeter:.2f}")


Circle = circle1()

Circle.area()
Circle.perimeter()