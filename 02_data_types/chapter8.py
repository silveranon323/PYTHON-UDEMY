ingredients=["Water","Milk","Black Tea"]
ingredients.append("Sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("Water")
print(f"Ingredients are: {ingredients}")
spice_options=["Ginger","Cardamon"]
chai_ingredients=["Water","Milk"]
chai_ingredients.extend(spice_options)
print(f"Chai {chai_ingredients}")
chai_ingredients.insert(2,"Black Tea")
print(f"Chai {chai_ingredients}")
last_added=chai_ingredients.pop()
print(f"Last added {last_added}")
print(f"Chai: {chai_ingredients}")
print(f"Chai: {chai_ingredients.reverse()}")
print(f"Chai: {chai_ingredients}")
print(f"Chai: {chai_ingredients.sort()}")
print(f"Chai: {chai_ingredients}")

sugar_levels=[1,2,3,4,5]
print(f"Maximum sugar level is {max(sugar_levels)}")
print(f"Minimum sugar level is {min(sugar_levels)}")

base_liquid=["Water","Milk"]
extra_flavour=["ginger"]
full_liquid_mix=base_liquid+extra_flavour
print(f"The full liquid is: {full_liquid_mix}")

strong_brew=["Black Tea","Water"] * 3
print(f"Strong brew {strong_brew}")

raw_spice_data=bytearray(b"Cinnamon")
raw_spice_data=raw_spice_data.replace(b"Cinna",b"Card")
print(f"Bytes: {raw_spice_data}")
