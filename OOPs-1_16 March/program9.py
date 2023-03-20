#OOPs-5
class Dam:
    def __init__(self, name, length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=Dam("ABC dam", 3.5 )
print ("Dam name:", dam1.name)
print("Dam Length", dam1.get_length())

class Table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
    def assign_data(self, glass_top,wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify_rate(self, glass_top, wooden_top):#
        self.assign_data(glass_top, wooden_top)
        if (self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate(False,True)
print(rate)
