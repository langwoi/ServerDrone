class Hero:
    def __init__ (self,Inputname,InputHealth,InputRt):
        self.name = Inputname
        self.health = InputHealth
        self.rt = InputRt

hero1 = Hero("Bambang Yono",150,5)
hero2 = Hero("BambangTedjo",200,90)

print(hero2.__dict__)
print(hero1.__dict__)
