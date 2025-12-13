
# This function will be tested automatically. 
# Do not change the function name or parameters.
def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
    # Write your code below this line
    result = []
    index = 0
    while index < len(withdrawals):
        amount = withdrawals[index]
        if amount <= balance:
            balance -= amount
            result.append(f"Withdrawn: {amount}")
        else:
            result.append(f"Insufficient funds for requested amount: {amount}")
        index += 1
    result.append(f"Remaining Balance: {balance}")
    return result