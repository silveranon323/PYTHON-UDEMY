chai_order=dict(type="Masala Chai" , size="Large" , sugar=2)
print(f"Chai order: {chai_order}")
chai_recipe={}
chai_recipe["Base"]="Black Tea"
chai_recipe["Liquid"]="Milk"
print(f"Recipe base: {chai_recipe['Base']}")
print(f"Liquid base: {chai_recipe['Liquid']}")
print(f"Recipe: {chai_recipe}")
del chai_recipe["Liquid"]
print(f"Recipe: {chai_recipe}")
print(f"Sugar is in the order? {"sugar" in chai_order}")
chai_order=dict(type="Ginger Chai" , size="Large" , sugar=1)
# print(f"Order details (Keys) : {chai_order.keys()}")
# print(f"Order details (Values) : {chai_order.values()}")
# print(f"Order details (Items) : {chai_order.items()}")

last_item=chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices={"Cardamom":"crushed" , "Ginger" : "Sliced"}
chai_recipe.update(extra_spices)
print(f"Updated chai recipe: {chai_recipe}")
customer_note=chai_order.get("note","No note")
print(f"Customer note is: {customer_note}")