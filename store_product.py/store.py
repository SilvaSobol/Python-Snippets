
import product


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
            print(f"The item sold sold is: {id}")
        return self
    
    def inflation(self,percent_increase = 0.02):
        if percent_increase:
            self.product_list += (self.price * percent_increase)
            print("oh NO!")
        return self


    def inventory(self):
        print(f"Store inventory{self.product_list}")



tj = Store("TRADER","list")
maxtrade = Store("Maxtrade","list")
bluecorn = Store("BlueCorn","list")



tj.add_product({'milk','bacon','cheese','cupcakes'}).sell_product('bacon').inflation().inventory()

milk.update_price(3).print_info()