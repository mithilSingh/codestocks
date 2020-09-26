# codestocks
class list_:
    def __init__(self,name_of_items,price_,number):
        self.main_list={}
        self.main_list[name_of_items]=[price_,number]

    def additems(self,new_item,price,no_of_items):
        self.ni=new_item
        self.price_of_itm=price
        self.no_item=no_of_items
        if self.ni not in self.main:
            self.main_list[self.ni]=[self.price_of_itm,self.no_item]

        else:
            self.main_list[self.ni][1]+=self.no_item

    def remove_items(self,item_name,price,no_of_items):
        self.ritem=item_name
        self.price_of_itm=price
        self.no_item=no_of_items
        try:
            if main_list[self.ni][1]>0:
                self.main_list[self.ritem][1]-=self.no_item
            else:
                return(f"There is no item such as {self.ritem}")
        except KeyError:
            return("Given item is not in the stocks ")
    def sell(self,asked_item):
        self.stock_item=asked_item
        try:
            if main_list[self.ni][1]>0:
                self.main_list[self.ritem][1]-=self.no_item
            else:
                return(f"There is no item such as {self.ritem}")

        except KeyError:
            return("Given item is not in our stocks ")
    def show_current_items_in_stocks(self):
        print("name","price","no. of them left")
        for i in self.main_list:
            print(i,self.main_list.get(i)[0],self.main_list.get(i)[1])
    def calculate(self,li):
        total_amount=0
        self.clist=li
        for ii in 

class people:
    def __init__(self,name_of_buyer):
        self.name=name_of_buyer
        self.cart={}
    def add_to_cart(self,item_to_add):

        self.to_add=item_to_add
        
        if self.to_add in self.cart:
            self.cart[self.to_add]+=1
        elif self.to_add not in self.cart:
            self.cart[self.to_add]=1
        else:
            print("the item was not added")
        return self.to_add    
    def remove_from_cart(self,item_to_add):
        self.to_add=item_to_add
        
        if self.to_add in self.cart:
            self.cart[self.to_add]-=1
        elif self.to_add not in self.cart:
            print(f"there was no such item as {self.to_add}in the cart")
        else:
            print("the item was not removed")
        return self.to_add    
    def show_current_items_in_cart(self):
        print("name","price")
        for i in self.cart:
            print(i,self.main_list.get(i))
    def finally_buy_it(self):
        return(cart)

    
