def make_chai():
    if not kettle_has_water:
        fill_water()
    plug_in_kettle()
    boil_water()
    if not is_cup_clean():
        wash_cup()
    add_to_cup("Tea_leaves")
    add_to_cup("sugar")
    pour("Boiled_water")
    stier("cup")
    serve("chai")


make_chai()