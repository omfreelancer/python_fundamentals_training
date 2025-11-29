class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount <= 0:
            return None
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        if amount <= 0 or amount > self.balance:
            return None
        
        self.balance -= amount
        return True
    
    def get_balance(self):
        return self.balance
    
    def show_info(self):
        return (f"Owner: {self.owner} | Balance: {self.balance:.2f}")