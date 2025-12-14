# chai="Ginger Chai"
# def prepare_chai(order):
#     print("Preparing",order)
# prepare_chai(chai)  
# print(chai)  

chai=[1,2,3]
def edit_chai(cup):
    cup[1]=42
edit_chai(chai)
print(chai)


def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)
make_chai("Darjelling","yes","low")
make_chai(milk="No",tea="Green",sugar="Medium") #keywords

def special_chai(*ingredients,**extras):
    print("ingredients",ingredients)
    print("extras",extras)

special_chai("Cinnamon","Cardimon","Rose",sweetner="Honey",foam="Yes")