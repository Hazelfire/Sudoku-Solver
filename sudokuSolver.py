
file = open("puzzle.txt", "r")
puzzleText = file.read()
puzzle = [[puzzleText.split("\n")[j][i] for i in range(9)] for j in range(9)] 

markings =[[set(["1", "2", "3", "4", "5", "6", "7", "8", "9"]) for i in range(9)] for j in range(9)]

def removeColumn(x, number):
    for y in range(9):
        if number in markings[y][x]:
            markings[y][x].remove(number)

def removeRows(y, number):
    for x in range(9):
        if number in markings[y][x]:
            markings[y][x].remove(number)

def removeSquare(x, y, number):
    squareCornerX = (x // 3)*3
    squareCornerY = (y // 3)*3

    for squareX in range(squareCornerX, squareCornerX + 3):
        for squareY in range(squareCornerY, squareCornerY + 3):
            if number in markings[squareY][squareX]:
                markings[squareY][squareX].remove(number)
    
def removeAll(x,y,number):
    removeColumn(x, number)
    removeRows(y, number)
    removeSquare(x,y,number)

def onlyInColumn(number, x):
    count = 0
    for y in range(9):
        if number in markings[y][x]:
            count +=1
    return count == 1

def onlyInRow(number, y):
    count = 0
    for x in range(9):
        if number in markings[y][x]:
            count +=1
    return count == 1

def onlyInSquare(number, x, y):
    squareCornerX = (x // 3)*3
    squareCornerY = (y // 3)*3

    count = 1
    for squareX in range(squareCornerX, squareCornerX + 3):
        for squareY in range(squareCornerY, squareCornerY + 3):
            if number in markings[squareY][squareX]:
                count += 1
    return count == 1



newElement = True
while newElement:
    newElement = False
    for x in range(9):
        for y in range(9):
            if puzzle[y][x] != " ":
                number = puzzle[y][x]
                markings[y][x] = set()
                removeAll(x,y,number)
    for x in range(9):
        for y in range(9):
            if len(markings[y][x]) == 1:
                nemElement = True
                number = markings[y][x].pop()
                puzzle[y][x] = number
                newElement = True
                removeAll(x,y,number)
            else:
                # Brute force test numbers
                for number in markings[y][x]:
                    if onlyInColumn(number, x) or onlyInRow(number, y) or onlyInSquare(number, x, y):
                        markings[y][x] = set()
                        puzzle[y][x] = number
                        newElement = True
                        removeAll(x,y,number)
                        break                        

print(markings)
for y in range(9):
    print(puzzle[y])
