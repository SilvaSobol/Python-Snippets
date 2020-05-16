
class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self,amount):
         self.account_balance += amount

    def make_withdrawal(self,amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User:{self.name}, Balance:${self.account_balance}")

    
    def transfare_fund(self, other_user,amount):
        other_user.make_deposit(amount) # other_user.account_balance += amount
        self.make_withdrawal(amount)    # self.account_balance -= amount


    
nick = User("Nick","nick@nick.com")
john = User("John","john@john.com")
sebastian = User("Sebastian","sebastian@email.com")
silva = User("Silva Sobol","silva@silva.com")


nick.transfare_fund(silva,100)
nick.make_deposit(100)
silva.make_deposit(1000)
nick.make_withdrawal(50)

nick.display_user_balance()
silva.display_user_balance()




