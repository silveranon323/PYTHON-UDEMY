# file=open("Order.txt","w")
# try:
#     file.write("Ginger tea - 2 cups")
# finally:
#     file.close()

with open("Orders.txt","w") as file:
    file.write("Ginger Tea - 2 Cups")

# behind the scenes file.__enter__()
# file.__exit__() is get called.