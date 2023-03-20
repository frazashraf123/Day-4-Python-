#OOPs-6
class Table:
    def __init__(self):
        print(id(self))
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
dining_table=Table()
back_table=Table()
front_table=back_table
back_table=dining_table
print(id(dining_table),id(back_table),id(front_table))#


        

























