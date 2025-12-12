class Chai:
    def __init__(self,sweetness,milk_level):
         self.sweetness=sweetness
         self.milk_level=milk_level
    def sip(self):
         print("Sipping chai")
    
    def add_sugar(self,amount):
         print("Added the sugar")

my_chai=Chai(sweetness=5,milk_level=10)
my_chai.add_sugar(2)
         