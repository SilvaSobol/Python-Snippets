class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
	
    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            print(f"Insufficient funds: Charging a $5 fee" and {self.amount-5})
        return self

    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self

    def yield_interest(self):
        # if self.balance > 0:
        #     self.balance = self.balance + self.balance * self.int_rate
        self.balance += self.balance * self.int_rate
        print(f"This is your account balance:{self.balance}")
        return self

acct_1 = BankAccount(.03,0)
acct_2 = BankAccount(.05,1000)

acct_1.deposit(3000000).deposit(10).withdraw(200).yield_interest().display_account_info()
acct_2.deposit(10000).deposit(100).withdraw(100).yield_interest().display_account_info()

		