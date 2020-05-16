import store
 

class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price=price
        self.category=category
    
    def update_price(self,percent_change = 0, is_increased = 0.03): 
        if is_increased:
            self.price += (self.price * percent_change)
            print("Price increased")
        else:
            self.price -= self.price * percent_change
        return self

    def print_info(self):
        print(f"Product:{self.name}, Category:{self.category}, Price:{self.price}")




milk = Product("Milk",1.99,"Dairy")
chicken = Product("Chicken",3.99,"Poultry")
bread = Product("Bread",3.00,"Bread and Pastry")
eggs = Product("Chocolate",2,"Candy")
lavash = Product("Nanak", 5.99,"Bakery")


tj.add_product({'milk','bacon','cheese','cupcakes'}).sell_product('bacon').inflation().inventory()
milk.update_price(3).print_info()