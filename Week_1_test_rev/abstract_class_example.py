from abc import ABC, abstractmethod
class Shape(abs):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length:int,breadth:int):
        self.length=length
        self.breadth=breadth
    def area(self):
        calculate_area=self.length*self.breadth
        return calculate_area
class Circle(Shape):
    def __init__(self,r:int):
        self.r=r
    def area(self):
       return 3.14 * self.r * self.r