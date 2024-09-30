from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    def area(self):
        print("AREA OF TRIANGLE")
        base = float(input("Enter the base"))
        height = float(input("Enter the height"))
        return base * height


class Rectangle(Shape):
    def area(self):
        print('AREA OF RECTANGLE')
        length = float(input("Enter the length"))
        breadth = float(input("Enter the breadth"))
        return length * breadth


class Square(Shape):
    def area(self):
        print('AREA OF SQUARE')
        side = float(input("Enter a side"))
        return side * side


t = Triangle()
print("The area of the triangle is: ", t.area())
r = Rectangle()
print("The area of the triangle is: ", r.area())
s = Square()
print("The area of the triangle is: ", s.area())
