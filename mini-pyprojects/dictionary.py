class list_:
    def __init__(self,name_of_items,price_,number):
        self.main_list={}
        self.n_o_i=number
        self.name=name_of_items
        self._price=price_
        if len(self.n_o_i)==len(self.name)==len(self._price):
            for i in range(len(self.n_o_i)):
                self.main_list[self.name[i]]=[self._price[i],self.n_o_i[i]]

    def additems(self,new_item,price,no_of_items):
        self.ni=new_item
        self.price_of_itm=price
        self.no_item=no_of_items
        if self.ni not in self.main_list:
            self.main_list[self.ni]=[self.price_of_itm,self.no_item]

        else:
            self.main_list[self.ni][1]+=self.no_item
    def returned_item(self,n_item,no_of_item):
        self.i_name=n_item
        self.no_of_item=no_of_item
        if self.i_name in self.main_list:
            self.main_list[self.i_name][1]+=self.no
        


        pass
 
    def sell(self,asked_item,no):
        self.stock_item=asked_item
        self.no=no
        try:
            if self.main_list[self.stock_item][1]>0:
                self.main_list[self.stock_item][1]-=self.no
            else:
                return(f"There is no item such as {self.stock_item}")

        except KeyError:
            print("Given item is not in our stocks ============================================")
            print(self.main_list)
    def show_current_items_in_stocks(self):
        print("name   ","| price |","no. of them left")
        for i in self.main_list:
            print(i,"   ",self.main_list.get(i)[0],"    ",self.main_list.get(i)[1])
            
    def calculate(self,li):
        self.total_amount=0
        self.clist=li
        for ii in self.clist:
            if ii in self.main_list:
                cfi=self.main_list[ii][0]*self.clist[ii]
                self.total_amount+=cfi
            elif ii not in self.main_list:
                print("item not in shop")
        return self.total_amount
    def give_currentlist(self):
        return self.main_list
        

class people:
    def __init__(self):
        self.cart={}
    def return_the_cart(self):
        return self.cart
    def add_to_cart(self,item_to_add,no_of_items):

        self.to_add=item_to_add
        self.no=no_of_items
        if self.to_add in self.cart  :
            self.cart[self.to_add]+=self.no
            return self.to_add 
        elif self.to_add not in self.cart:
            self.cart[self.to_add]=self.no
            return self.to_add
        else:
            print("the item was not added")
            
    def remove_from_cart(self,item_to_add,no_of_items):
        self.to_add=item_to_add
        self.no=no_of_items
        if self.to_add in self.cart :
            self.cart[self.to_add]-=self.no
            return self.to_add 
        elif self.to_add not in self.cart:
            print(f"there was no such item as {self.to_add}in the cart")
        
        elif self.cart[self.to_add]-self.no<=0:
            print(f"please have less no of {self.to_add}s")
        else:
            print("the item was not removed")
          
    def show_current_items_in_cart(self):
        print("name","no. of item")
        for i in self.cart:
            print(i,self.cart.get(i))
        
    def finally_buy_it(self):
        return(self.cart)
d_shop=list_(['broccoli', 'cabbage', 'carrot', 'cauliflower', 'corn', 'cucumber', 'mushroom', 'onion', 'pea', 'bean', 'potato', 'pumpkin',
 'radish', 'tomato', 'zucchini'],
 [165, 178, 56, 188, 21, 88, 124, 71, 36, 100, 60, 65, 92, 158, 78],
[100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
d_person=people()
while True:
    print('''
    enter \'Shop\' to purchase items from the default shop
    enter \'Shop from (name of the shop)\' to purchase items from user created shop
    enter \'Create new shop \' to create new shop 
    enter \'Leave \' to leave the program''')
    mi=input("->")
    if mi.upper()=="SHOP":
        while True:
             
            print('''
            Press \'V\' to view items in the shop
            Press \'A\' to add items to the cart
            Press \'R\' to remove items from the cart
            Press \'B\' to buy the items in the cart
            Press \'C\' to view the items in the cart
            Press \'Q\' to quit''')
            si=input(">")
            if si.upper()=="V":
                d_shop.show_current_items_in_stocks()
            elif si.upper()=="A":
                ck=True
                while ck==True:
                    a=input('enter the name of item:').lower()
                    
                    while True:
                        b=int(input(f'enter the number of {a}:'))
                        try:
                            if b>(d_shop.give_currentlist())[a][1]:
                                print(f"please buy less number of {a}s")
                            else:
                                d_shop.sell(d_person.add_to_cart(a,b),b)
                                print(d_person.show_current_items_in_cart())
                                ck=False
                                break
                            
                        except KeyError:
                            print(f"there is no such item as {a} in the shop")
                            break
                    
            elif si.upper()=="C":
                d_person.show_current_items_in_cart()
            elif si.upper()=="B":
                print("current in your cart========")
                d_person.show_current_items_in_cart()
                print("total price-",d_shop.calculate(d_person.finally_buy_it()))
        
            elif si.upper()=="R":
                while True:
                    d=input("Enter the name of item:")
                    
                    if  d in d_person.return_the_cart() :
                        
                        while True:
                            e=int(input(f"Enter the number of {d}:"))
                            if d_person.return_the_cart()[d]>=e:
                                d_shop.returned_item(d_person.remove_from_cart(d,e),e)
                                break
                            else:
                                print(f"you dont have that much number of {d}")
                        break
                    else:
                        print("there is no such item in your cart")
            elif si.upper()=="Q":
                print("thank you for shoping")
                break     
 
    elif mi[0:10].lower()=="shop from ":
        pass
    elif mi.lower()=="create new shop":
        pass
    elif mi.lower()=="leave":
        break
        
