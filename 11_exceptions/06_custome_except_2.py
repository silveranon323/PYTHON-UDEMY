class Out_of_ingredients(Exception):
    pass
def make_chai(milk,sugar):
    if milk==0 or sugar==0:
        raise Out_of_ingredients("Insufficients ingredients.")
    print("Good to go lets make chai.")
make_chai(0,1)