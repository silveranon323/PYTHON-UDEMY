# essential_spices={"Cardamon","Ginger","Cinnamon"}
# optional_spices={"Cloves","Ginger","Black Pepper"}
# all_spices=essential_spices | optional_spices
# print(f"All spices: {all_spices}")
# common_spices=essential_spices & optional_spices
# print(f"Common spices: {common_spices}")
# only_in_essential=essential_spices-common_spices
# print(f"Only in essential spices:{only_in_essential}")
# print(f"is cloves in optional spices?{"Cloves" in optional_spices}")

branch_a_products={"bread", "milk", "butter", "jam"}
branch_b_products={"bread", "cheese", "butter", "ketchup"}
print(branch_a_products)
print(branch_b_products)
unionn=branch_a_products.union(branch_b_products)
print(unionn)
print(branch_a_products.intersection(branch_b_products))
print((branch_a_products & branch_b_products) - branch_a_products)
essential_items=frozenset(["milk","bread","ketchup"])
print(essential_items)