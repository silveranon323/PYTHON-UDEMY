class BankAccount:
    def __init__(self,owner_name:str,balance:int):
        self.owner_name=owner_name
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def deposit(self,amount:int):
        if amount>0:
            self.__balance+=amount
        else:
            raise ValueError("Amount cannot be negative.")
    def withdraw(self,amount:int):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount

account1=BankAccount("Alex",1000)
account1.deposit(500)
account1.withdraw(300)
print(f"Final balance after withdrawl is : {account1.get_balance()}")
