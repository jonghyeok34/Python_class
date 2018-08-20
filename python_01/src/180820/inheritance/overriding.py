# method overriding

class Star:
    def attack(self):
        print("스타의 어택")

class Terran(Star):
    def attack(self):
        print("테란 어택")

class Zerg(Star):
    def attack(self):
        print("저그의 어택")

if __name__ =="__main__":
    s= Star()
    t = Terran()
    z = Zerg()
    s.attack()
    t.attack()
    z.attack()