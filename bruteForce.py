file = open("puzzle.txt", "r")
puzzleText = file.read()
puzzle = [[puzzleText.split("\n")[j][i] for i in range(9)] for j in range(9)] 




def validInColumn(x, number):
    for y in range(9):
        if number == puzzle[y][x]:
            return False
    return True

def validInRow(y, number):
    for x in range(9):
        if number == puzzle[y][x]:
            return False
    return True

def validInSquare(x, y, number):
    squareCornerX = (x// 3)*3
    squareCornerY = (y // 3)*3

    for squareX in range(squareCornerX, squareCornerX + 3):
        for squareY in range(squareCornerY, squareCornerY + 3):
            if number == puzzle[squareY][squareX]:
                return False
    return True

def validPlacement(x,y,number):
    return validInColumn(x, number) and validInRow(y, number) and validInSquare(x,y,number)

originalSquares = []
for x in range(9):
    for y in range(9):
        if puzzle[y][x] != ' ':
            coords = x,y
            originalSquares.append(coords);

x = 0
y = 0
solved = False

def forward():
    global x,y
    if x < 8:
        x +=1
    else:
        y +=1
        x=0

def backward():
    global x,y
    if x == 0:
        y -= 1
        x = 8
    else:
        x -= 1

stack = []

while not solved:
    if (x,y) in originalSquares or puzzle[y][x] != " ":
        forward()
        continue
    for number in range(1,10):
        if validPlacement(x,y,str(number)):
            puzzle[y][x] = str(number)
            stack.append((x,y))
            forward()
            break
    else:
        # We couldn't do it, we need to backtrack
        found = False
        while not found:
            if len(stack) == 0:
                print("Done")
                quit()
            x,y = stack.pop()
            lastNumber = int(puzzle[y][x])

            for number in range(lastNumber + 1, 10):
                if validPlacement(x,y,str(number)):
                    puzzle[y][x] = str(number)
                    stack.append((x,y))
                    forward()
                    found = True
                    break
            else:
                puzzle[y][x] = " "
    if x == 0 and y == 9:
        # Solved!, lets find another solution
        for y in range(9):
            print("".join(puzzle[y]))
        found = False
        print()
        while not found:
            if len(stack) == 0:
                print("Done")
                quit()
            x,y = stack.pop()
            lastNumber = int(puzzle[y][x])

            for number in range(lastNumber + 1, 10):
                if validPlacement(x,y,str(number)):
                    puzzle[y][x] = str(number)
                    stack.append((x,y))
                    forward()
                    found = True
                    break
            else:
                puzzle[y][x] = " "
