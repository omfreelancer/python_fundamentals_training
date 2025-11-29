class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return None
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance or amount <=0:
            return False
        
        self.balance -= amount
        return True
    
    def get_balance(self):
        return self.balance
    
    def show_info(self):
        return f"Owner: {self.owner} | Balance: {self.balance:.2f}"
    
class Bank:
    def __init__(self, accounts=None):
        self.accounts = {} if accounts is None else accounts

    def create_account(self, owner, initial_balance=0):
        if owner in self.accounts:
            return None
        
        self.accounts[owner] = BankAccount(owner, initial_balance)
        return self.accounts[owner]
    
    def find_account(self, owner):
        if owner in self.accounts:
            return self.accounts[owner]
        
        return None
    
    def deposit_to(self, owner, amount):
        account = self.find_account(owner)
        if account is None:
            return f"No account found for: {owner}"
        
        deposite = account.deposit(amount)
        
        if deposite is None:
            return "Amount must be more than 0."
        
        return f"Deposited {amount:.2f} to {owner}"
    
    def withdraw(self, owner, amount):
        account = self.find_account(owner)
        if account is None:
            return f"No account found for: {owner}"
        
        withdraw = account.withdraw(amount)
        if not withdraw:
            return f"Insufficient balance for {owner}."
        return f"Withdrew {amount:.2f} from {owner}"
    
    def show_all_accounts(self):
        return [account.show_info() for account in self.accounts.values()]