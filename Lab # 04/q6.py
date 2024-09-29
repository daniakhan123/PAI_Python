class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, initial_balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds for the withdrawal.")
        else:
            print("Withdrawal amount must be greater than zero.")

    def check_balance(self):
        
        print(f"Account balance: ${self.balance:.2f}")



account = BankAccount(account_number="123456", customer_name="Dania Khan", date_of_opening="2024-09-10", initial_balance=1000.0)

account.check_balance()
account.deposit(2367.0)
account.withdraw(599.0)
account.check_balance()
account.withdraw(1500.0)
