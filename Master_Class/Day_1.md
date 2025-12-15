

Variables and Datatypes

Python is a dynamically typed language

a=10
b=20
is_dev=True

In future this dynamically typing will be a cause for some silence bugs in future.


Strings:

Anything that represents text is called as strings could be name,email,passwords.

first_name="Hem"
last_name="Pradhan"

full_name=first_name+""+last_name

cleaner way to print strings:

print(f"My name is {full_name}! I am a Python student")


List and Dictionaries:

List stores ordered collections
skills=["Python","Sql","DSA"]
print(skills[0])

Dictionaries:
backbone of apis
key value pairs

user={
    "name":"HEM",
    "age":22,
    "City":"Jamshedpur"
}

print(user["name"])


Input/Output

name=input("enter name: ")
print(f"welcome {name}")
age=int(input("Enter your age: "))
print(age)

note:Always have conversions ready


Operators:

Tell python to perform actions

a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
the above all are called as arithmetic operators

a>b
a<b
a==b
a!=b

the above all are the comparisons operators

Control Flow:
i)Conditonals
age=int(input(Enter your age: ))
if age>=18:
    PRINT("yOU CAN VOTE)
else:
print("You are under age.)

if marks>=90:
print("A")
elif marks>=75:
    print("B+")


Loops:
for i in range(5):
    print(i)

o/p:01234 ending is exclusive not inclusive

i=0
while(i<5):
    print(i)
    i+=1


Functions:
write a code once and write it anywhere
used for making code reusable and readable.

syntax:
def greet_name(name):
    return f"Hello {name}"

print(greet_name("Hem"))

def add(a:int,b:int)->int:
    return a+b

the above is known  as type hints 
they improve code redability and catches early bugs a type to write production ready code and to catch bugs easily.


OOPS:
classes and objects
oops->models->Real world entity

class->the actual blueprint that we use
object -> they are the instance of the classes

attributes and methods
class:
variables: attributes of class
functions:methods

class User:
    def set_name(self,name:str):
        self.name=name
        return f"Hello i am {self.name}"
u=User()
u.set_name()

class User:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
constructors(__init___)


Encapsulation:
binding data into single unit



class Bank:
    def __init__(self,balance:int):
        self._balance=balance
        #here underscore means internal use
    def deposit(self,amount:int):
        if amount<=0:
            raise valueError("Invalid Amount")
        self.balance+=amount














