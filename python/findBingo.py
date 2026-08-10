class Coord():
    def __init__ (self, x: float, y: float):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"coord: {self.x}, {self.y}"

coord1 = Coord(1.0 , 2.0)
coord2 = Coord(9.0, 8.0)

everyName = ["Sigma", "bingo"]
everyPosition = [coord1, coord2]

def getPosition(name:str):
    count = 0
    name = name
    coord = 0
    found = False
    while count < len(everyName) and found == False:
        if everyName[count] == name:
            coord = count
            found = True
        count += 1
    result = everyPosition[coord]
    return result
        
#i need the position of bingo
print(getPosition("bingo"))

