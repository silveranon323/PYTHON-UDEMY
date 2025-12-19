def brew_chai(flavour):
    if flavour not in ["Masala","Elaichi","Ginger"]:
        raise ValueError("Sorry we dont have that flavour.")
    print(f"Brewing {flavour} chai.")
brew_chai("Mint")