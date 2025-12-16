from abc import ABCMeta , abstractmethod  # used for abstraction in python
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        return 0
class Square(Shape):
    side=4
    def area(self):
        print("Area of square is " , self.side*self.side)
class Rectangle(Shape):
    width=5
    length=10
    def area(self):
        print("Area of rectangle",self.length*self.width)
square=Square()
rectangle=Rectangle()
square.area()
rectangle.area()
