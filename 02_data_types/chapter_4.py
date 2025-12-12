is_boiling=True
stri_count=5
total_actions=stri_count+is_boiling  # upcasting
print(f"total actions : {total_actions}")
milk_present=1 # only handful values represent false 0,none rest results True
print(f"is there milk present?{bool(milk_present)}")

water_hot=True
tea_added=True
print(f"Can serve chai?{water_hot and tea_added}")