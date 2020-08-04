from tkinter import *
import random
import time

WIDTH = 400
HEIGHT = 400
field = []
newField = []
size = 20

def fill(field, chance):
    for i in range(0, len(field)):
        for j in range(0, len(field[i])):
            if (random.randint(0, 100) < chance):
                field[i][j] = 1
            else:
                field[i][j] = 0

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

def initField(field, w, h):
    for i in range(0, w):
        field.append([])
        for j in range(0, h):
            field[i].append(0)

def drawBorders(field, canvas, size):
    # Vertical
    for i in range(0, len(field)):
        canvas.create_line(i * size, 0, i * size, 400-size)
    # Horizontal
    for i in range(0, len(field[0])):
        canvas.create_line(0, i * size, 400-size, i * size)

def drawField(field, canvas, size):
    canvas.delete(ALL)
    for i in range(0, len(field)):
        for j in range(0, len(field[i])):
            if (field[i][j] == 1):
                canvas.create_rectangle(i * size, j * size, i * size + size, j * size + size, outline="white", fill="red")
            else:
                canvas.create_rectangle(i * size, j * size, i * size + size, j * size + size, fill="black")

def pentadecathlon(field, x, y):
    field[x + 2][y] = 1
    field[x + 1][y + 1] = 1
    field[x][y + 2] = 1
    field[x][y + 3] = 1
    field[x][y + 4] = 1
    field[x][y + 5] = 1
    field[x][y + 6] = 1
    field[x][y + 7] = 1
    field[x + 1][y + 8] = 1
    field[x + 2][y + 9] = 1
    field[x + 3][y + 8] = 1
    field[x + 4][y + 7] = 1
    field[x + 4][y + 6] = 1
    field[x + 4][y + 5] = 1
    field[x + 4][y + 4] = 1
    field[x + 4][y + 3] = 1
    field[x + 4][y + 2] = 1
    field[x + 3][y + 1] = 1

def glider(field, x, y):
    field[x + 1][y] = 1
    field[x + 2][y + 1] = 1
    field[x + 2][y + 2] = 1
    field[x + 1][y + 2] = 1
    field[x][y + 2] = 1

def click():
    global newField
    global field
    global size
    generation(field, newField)
    drawField(field, canvas, size)

def relaunch():
    global field
    global size
    fill(field, 15)
    drawField(field, canvas, size)

if __name__ == '__main__':
    window = Tk()
    window.geometry("800x600")
    window.title("Life")
    
    leftFrame = Frame(window)    
    rightFrame = Frame(window)

    canvas = Canvas(leftFrame, width=HEIGHT, height=HEIGHT)
    button = Button(rightFrame , text="Следующее поколение!", command=click)
    button2 = Button(rightFrame , text="Пересоздать!", command=relaunch)
    rightFrame.pack(side=RIGHT)
    leftFrame.pack(side=LEFT)
    canvas.pack()
    button.pack(side=TOP)
    button2.pack(side=TOP)

    initField(field, 20, 20)
    initField(newField, 20, 20)
    #drawBorders(field, canvas, size
    fill(field, 15)
    drawField(field, canvas, size)
    #pentadecathlon(field, 3, 3)
    #glider(field, 10, 10)

    window.mainloop()
