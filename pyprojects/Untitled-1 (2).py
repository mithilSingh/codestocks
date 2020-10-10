class Animal:
    def __init__ (self,which_animal,name,age):
        self.name=name
        self.animal=which_animal
        self.age=age
    def get_the_name(self):
        print(self.name)
    def get_the_age(self):
        print(self.age)
    def get_the_animal(self):
        print(self.animal)
A1=Animal("dog","hachi",4)
A1.get_the_age()
    
        