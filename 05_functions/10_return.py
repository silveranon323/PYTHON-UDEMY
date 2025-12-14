def make_chai():
    print("Here is your masala chai.")
return_value=make_chai()
print(return_value)

def idle_chai_wla():
    pass
print(idle_chai_wla())

def sold_cups():
    return 120

total=sold_cups()
print(total)


def chai_status(cups_left):
    if cups_left==0:
        return "Sorry chai over."
    return "Chai is ready!"
print(chai_status(10))

def chai_report():
    return 120,69,70

sold,remaining,not_paid=chai_report()
print("Sold:",sold)
print("Remaining:",remaining)