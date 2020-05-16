class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price 
        self.category = category

    def update_price(self,percent_change = 0, is_increased = 0.03):
        if is_increased:
            self.price += self.price * percent_change
            print("Price increased")
        else:
            self.price -= self.price * percent_change
        return self

    def print_info(self):
        print(f"Product:{self.name},Category:{self.category},Price: {self.price}")

    
class Store:
    def __init__(self,name,product_list):
        self.name = name
        self.product_list = {product_list}
        
    def add_product(self,new_product):
        self.product_list = new_product
        return self
    
    def sell_product(self,id):
        if id in self.product_list:
            self.product_list.remove(id)
            print(f"The item sold was: {id}")
        return self

    def inflation(self,percent_increase = 0.02):
        if percent_increase:
            self.product_list += self.price * percent_increase
            print("oh NO!")
        return self

    def inventory(self):
        print(f"Storre inventory{self.product_list}")


milk = Product("Milk",3.99,"Dairy")
egg = Product("Egg",4.00,"Dairy")
bread = Product("Bread", 2.99,"Bakery")
cheese = Product("Manari",4.99,"Dairy")
chicken = Product("Chicken",3.99,"Poultry")
chocolate = Product("M&M's",2,"Candy")
lavash = Product("Nanak", 5.99,"Bakery")

tj = Store("Trader","Inventory")
maxtrade = Store("Maxtrade","Inventory")
bluecorn = Store("BlueCorn","Inventory")



tj.add_product({'milk','bacon','cheese','cupcakes'}).sell_product('bacon').inflation().inventory()
milk.update_price(3).print_info()


