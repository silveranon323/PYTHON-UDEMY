# This function will be tested automatically.
# Do not change the function name or parameters.
 
loyalty_points = 0  # global variable
 
def process_transactions(transactions: list[int]) -> int:
    # Write your code below this line
    def apply_bonus():
        nonlocal total
        if total > 1000:
            total += 50  # bonus for high spenders
 
    total = 0
 
    for amount in transactions:
        total += amount
 
    apply_bonus()
 
    # update global loyalty_points
    global loyalty_points
    loyalty_points += total // 100  # earn 1 point per ₹100
 
    return total