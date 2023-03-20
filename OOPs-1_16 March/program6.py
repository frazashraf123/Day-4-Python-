#OOPS-2

class Book: 
    def __init__(self):
        self.title=None
my_fav=Book()                                                                               

my_fav.title="Head first programming"
your_fav=Book()
your_fav.title="Learning Python in the hard way"
my_fav.title="Learning Python"
print("My favourite is",my_fav.title)
print("Your's is",your_fav.title)

class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
s1=Shoe(1000,"Canvas")
print(s1)
print(s1.price,s1.material)
print(id(s1))
