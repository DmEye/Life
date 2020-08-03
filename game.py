import os
import random
import time

field = [[],
         [],
         [],
         [],
         [],
         [],
         [],
         [],
         [],
         []
        ]
newField = [
         [],
         [],
         [],
         [],
         [],
         [],
         [],
         [],
         [],
         []
        ]
n = 40
live = True
score = 0

def create(field, newField, n):
    for i in range(0, len(field)):
        for j in range(0, n):
            field[i].append(0)
            newField[i].append(0)

def fill(field, chance):
    for i in range(0, len(field)):
        for j in range(0, len(field[i])):
            if (random.randint(0, 100) < chance):
                field[i][j] = 1

def draw(field):
    global score
    if (os.uname().sysname == "Linux"):
        os.system("clear")
    else:
        os.system("cls")
    for i in range(0, len(field)):
        buffer = ""
        for j in range(0, len(field[i])):
            if (field[i][j] == 1):
                buffer += "x"
            else:
                buffer += " "
        print(buffer)
    print("Поколение: " + str(score))
    time.sleep(0.1)
    score += 1

def neighbours(field, x, y):
    count = 0
    for i in range(-1, 2):
        newx = (x - i + len(field)) % len(field)
        for j in range(-1, 2):
            newy = (y - j + len(field[i])) % len(field[i])
            if (field[newx][newy] == 1 and (i != 0 or j != 0)):
                count += 1
    return count

def generation(field, newField):
    for i in range(0, len(field)):
        for j in range(0, len(field[i])):
            c = neighbours(field, i, j)
            if (field[i][j] == 0):
                if (c == 3):
                    newField[i][j] = 1
            if (field[i][j] == 1):
                if (c < 2 or c > 3):
                    newField[i][j] = 0
                else:
                    newField[i][j] = field[i][j]
    for i in range(0, len(field)):
        for j in range(0, len(field[i])):
            field[i][j] = newField[i][j]

def logic():
    global field
    global newField
    global live
    for i in range(0, len(field)):
        for j in range(0, len(field[i])):
            if (field[i][j] == 1):
                return
    live = False

def glider(field, x, y):
    field[x + 1][y] = 1
    field[x + 2][y + 1] = 1
    field[x + 2][y + 2] = 1
    field[x + 1][y + 2] = 1
    field[x][y + 2] = 1

if __name__ == "__main__":
    create(field, newField, n)
    fill(field, 30)
    #glider(field, 4, 4)
    draw(field)
    while (live):
        logic()
        generation(field, newField)
        draw(field)
    input("Конец! Нажми Enter...")
