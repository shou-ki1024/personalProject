class Player:
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.health = health
        
class Tittlehead:
    def _init_(self):
        pass
    def show(self, name):
        self.name = name

p1 = Player(input("enter your name"), input("age:"), input("health:"))
print("your name has been confirmed", p1.name, p1.age, p1.health)