def process_order(item,quantity):
    try:
        price={"masala":20,"ginger":40}[item]
        cost=price*quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not available in the menu")
    except TypeError:
        print("Quantity must be in number")
process_order("ginger",2)