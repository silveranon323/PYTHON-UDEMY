# public => membername
# protected=>_member_name
# private=> __member_name

class Car:
    number_of_wheels=4
    _color="Black"
    __yearofmanufacture=2017
class Bmw(Car):
    def __init__(self):
        print("Protected  attribute color : " , self._color)
car=Car()
print("Public attribute no of wheels" , car.number_of_wheels)
bmw=Bmw()
print("private attribute year of manufacture" ,  car.__yearofmanufacture)
         
