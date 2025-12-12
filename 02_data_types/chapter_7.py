masala_spices=("cardamom","ginger","cinnamon")
spice_1,spice_2,spice_3=masala_spices
print(f"Main masala spices are : {spice_1} , {spice_2} , {spice_3}")
ginger_ratio,cardamom_ratio=2,1
print(f"Ratio is G :{ginger_ratio} and C: {cardamom_ratio}")
ginger_ratio,cardamom_ratio=cardamom_ratio,ginger_ratio
print(f"Ratio is G :{ginger_ratio} and C: {cardamom_ratio}")

# membership

print(f"is ginger in masala spices ? {'ginger' in masala_spices}")