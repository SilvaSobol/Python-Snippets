class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        self.accounts =[]

    def create_account(self, id):
        self.account_number = account_number(id)
        self.accounts.append(account_number)

    def deposit(self, amount):
        self.balance += amount
        return self
	
    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            self.amount -= 5
            print(f"Insufficient funds: Charging a $5 fee")
            return self

    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self

    def yield_interest(self):
        # if self.balance > 0:
        #     self.balance = self.balance + self.balance * self.int_rate
        self.balance += self.balance * self.int_rate
        print(f"This is your interest rate:{self.balance}")
        return self

class User:
    def __init__(self,name,email,id):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)
        self.id = customer_id

    def make_deposit(self,amount,id):
        if self.id == id:
           self.account.deposit(100)    
           print(self.account.balance)
        else: 
            print("Ooops! Wrong account!")
        return self 

    def make_withdrawal(self,amount,id):
        if self.id == id:
            self.account.withdraw(33)
            print(f"Your balance is:${self.account.balance}")
        else:
            print("Something went wrong, please check your account number.")
        return self 

    def display_account_info(self):
        print(f"Balance:${self.account.balance}")
        return self


    def transfare_fund(self, other_user,amount):
        other_user.make_deposit(amount) # other_user.account_balance += amount
        self.make_withdrawal(amount)    # self.account_balance -= amount
        return self


    
nick = User("Nick","nick@nick.com",123)
john = User("John","john@john.com")
sebastian = User("Sebastian","sebastian@email.com")
silva = User("Silva Sobol","silva@silva.com")
george = User("George", "george@george.com ")




nick.make_deposit(1000000).make_withdrawal(999).make_deposit(0.99).transfare_fund(silva,500).display_account_info()

silva.make_deposit(10000).transfare_fund(sebastian,100).display_account_info()

sebastian.make_deposit(4000).display_account_info()


# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to