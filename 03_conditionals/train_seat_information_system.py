seat_type=str(input("Enter the seat type(sleeper/AC/genral/luxury): ")).lower()
match seat_type:
    case "sleeper":
        print("Sleeper - No AC  , Beds available")
    case "ac":
        print("AC-Air Conditioned , compfy ride.")
    case "general":
        print("General - cheapest option , no reservation")
    case "luxury":
        print("Premium seat with meals.")
    case _:
        print("Invalid seat type.")

