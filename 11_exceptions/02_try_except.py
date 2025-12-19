chai_menu={
    "masala":30,
    "ginger":40
}

try:
    print(chai_menu["Lemon Tea"])
except KeyError :
    print("The key you are trying to access doesn't exist")
print("Now the code will run without errors")