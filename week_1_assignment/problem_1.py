class Customer:
    def __init__(self, id: int, name: str, email: str, active: bool):
        self.id = id
        self.name = name
        self.email = email
        self.active = active

    def __repr__(self):
        status = "Active" if self.active else "Inactive"
        return f"Customer Id: {self.id}, Name: {self.name}, Email: {self.email}, Status: {status}"


def filter_active_customers(customers):
    return [c for c in customers if c.active]


def search_customer_by_name(name, customers):
    for customer in customers:
        if customer.name.casefold() == name.casefold():
            return customer
    return None


def sort_customers_by_name(customers):
    return sorted(customers, key=lambda c: c.name)


def print_customers(customers):
    if not customers:
        print("No customers found.")
    for c in customers:
        print(c)


# Customer data
customers = [
    Customer(1, "Hem Kishore Pradhan", "hemkishore@test.com", True),
    Customer(2, "Ananya Sharma", "ananya.sharma@gmail.com", True),
    Customer(3, "Rahul Verma", "rahul.verma@yahoo.com", False),
    Customer(4, "Priya Nair", "priya.nair@outlook.com", True),
    Customer(5, "Amit Patel", "amit.patel@gmail.com", True),
    Customer(6, "Sneha Iyer", "sneha.iyer@test.com", False),
    Customer(7, "Rohit Singh", "rohit.singh@gmail.com", True),
    Customer(8, "Kavya Mehta", "kavya.mehta@outlook.com", True)
]


# Menu-driven program
while True:
    print("\n===== CUSTOMER MANAGEMENT MENU =====")
    print("1. View all customers")
    print("2. View active customers")
    print("3. Search customer by name")
    print("4. Sort customers by name")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n**** ALL CUSTOMERS ****")
        print_customers(customers)

    elif choice == "2":
        print("\n**** ACTIVE CUSTOMERS ****")
        active_customers = filter_active_customers(customers)
        print_customers(active_customers)

    elif choice == "3":
        name = input("Enter customer name to search: ")
        result = search_customer_by_name(name, customers)
        if result:
            print("\nCustomer Found:")
            print(result)
        else:
            print("\nCustomer not found.")

    elif choice == "4":
        print("\n**** SORTED CUSTOMERS (BY NAME) ****")
        sorted_customers = sort_customers_by_name(customers)
        print_customers(sorted_customers)

    elif choice == "5":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1 and 5.")


# Pseudo REST API Contract

# GET /customers
# Description: Fetch all customers

# GET /customers?active=True
# Description: Fetch only active customers

# GET /customers/search?name=abc
# Description: Search a customer by name.