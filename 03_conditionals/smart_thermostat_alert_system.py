device_status=str(input("Enter the device status: "))
tempreature=int(input("Enter the tempreature: "))
if device_status == "active":
    if tempreature>35:
        print("Warn: High Tempreature.")
    else:
        print("Tempreature normal.")
else:
    print("Device is offline.")