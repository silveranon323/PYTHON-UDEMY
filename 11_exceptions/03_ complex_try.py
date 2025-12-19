def serve_chai(flavour):
    try:
        print(f"Preparing chai {flavour}")
        if(flavour=="unknown"):
            raise ValueError("We dont have that flavour")
    except ValueError as e:
        print("Error",e)
    else:
        print(f"{flavour} chai is served.")
    finally:
        print("Next customer please.")
serve_chai("masala")
serve_chai("unknown")