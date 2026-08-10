import random
menuAvail = ["check if your number is even or odd", "walk", "know your place", "bingo", "exit"]

def menuOptions():
    block = "======================="
    print(block)
    for i in range(len(menuAvail)):
        if i != len(menuAvail) - 1:
            print(f"{i+1}. {menuAvail[i]}")
        else:
            print(f"0. {menuAvail[i]}")
    print(block)

#getInput() belum dynamic.
def getInput():
    choice = int(input("enter your input('number'): "))
    if 0 <= choice <= len(menuAvail) - 1:
        match choice:
            case 0:
                exit()
            case 1:
                checkBilBulat()
            case 2:
                walk()
            case 3:
                where()
            case 4:
                bingo()
    else:
        print("none of options")

#List prosedur dan function.
def checkBilBulat(n: int = 0):
    n = int(input("masukkan nilai bilangan bulat('int'):  "))
    if n % 2 == 0:
        print("even")
    else:
        print("odd")

def walk():
    def randomizer():
        x = random.randint(1, 10)
        if x <= 5:
            print(f"you had a good luck 2 / 2")
            return 1
        else:
            print(f"bad ahh luck 1 / 2")
            return 0
    if randomizer() == 1:
        print("you walked like a pro")
    else:
        print("you're trying to walk, but you fell, Nice try!")

def where():
    class coord:
        def __init__(self, x: float, y: float):
            self.x = x
            self.y = y
        def __repr__(self):
            return f"coord x={self.x}, y={self.y}"
    coord1 = coord(8.0, 12.0)
    coord2 = coord(10.0, 20.0)
    mid = coord(0.0, 0.0)
    def know(coord1:coord, coord2:coord):
        mid.x = (coord1.x + coord2.x)/2
        mid.y = (coord1.y + coord2.y)/2
        result = coord(mid.x, mid.y)
        return result
    
    result = know(coord1, coord2)
    print(result)


menuOptions() 
getInput()

