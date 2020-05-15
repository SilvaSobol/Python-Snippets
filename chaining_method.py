class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self,amount):
         self.account_balance += amount
         return self 

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self 

    def display_user_balance(self):
        print(f"User:{self.name}, Balance:${self.account_balance}")
        return self

    
    def transfare_fund(self, other_user,amount):
        other_user.make_deposit(amount) # other_user.account_balance += amount
        self.make_withdrawal(amount)    # self.account_balance -= amount
        return self


    
nick = User("Nick","nick@nick.com")
john = User("John","john@john.com")
sebastian = User("Sebastian","sebastian@email.com")
silva = User("Silva Sobol","silva@silva.com")
george = User("George", "george@george.com ")




nick.make_deposit(1000).make_withdrawal(100).make_deposit(1000).transfare_fund(silva,300).display_user_balance()

silva.make_deposit(10000).transfare_fund(sebastian,100).display_user_balance()

sebastian.make_deposit(4000).display_user_balance()
