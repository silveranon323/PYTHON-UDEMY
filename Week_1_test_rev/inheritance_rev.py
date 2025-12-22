class Animal:
    def speak(self):
        print("Animal speaks!")
class Dog(Animal):
    def speak(self):
        print("Dog barks!")

# polymorphism example
class Cat(Animal):
    def speak(self):
        print("Cat meows!")
animals=[Dog(),Cat()]
for animal in animals:
    animal.speak()