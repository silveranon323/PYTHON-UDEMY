class InvalidChaiError(Exception):pass
def bill(flavour,cups):
    menu={"masala":20,"ginger":40}
    try:
        if flavour not in menu:
            raise InvalidChaiError("That chai is not in the menu.")
        if not isinstance(cups,int):
            raise TypeError("Quantity of cups must be an integer.")
        total=menu[flavour]*cups
        print(f"Your total bill is {total}")    
    except Exception as e:
        print("Errors",e)

    finally:
        print("Thanks for visiting us!")
bill("ginger","2")
bill("mint",40)
bill("masala",2)