def update_order():
    chai_type= "Elaichi"
    def kitchen():
        nonlocal chai_type #inside to inside function
        chai_type="Kesar"
    kitchen()
    print("After kitchen update " , chai_type)
update_order()