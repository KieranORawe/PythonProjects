from tkinter import *
import math
import random

window = Tk()
canvas = Canvas(window, width=1000,height=1000, background="white")
canvas.pack()

iterations = 10
linewidth = 2
color = "red"

angle = (360/iterations)
angle = math.radians(angle)
#print(angle)

wall = [
    [10,10,990,10],
    [990,10,990,990],
    [990,990,10,990],
    [10,990,10,10],
    [random.randint(10,990),random.randint(10,990),random.randint(10,990),random.randint(10,990)],
    [random.randint(10,990),random.randint(10,990),random.randint(10,990),random.randint(10,990)],
    [random.randint(10,990),random.randint(10,990),random.randint(10,990),random.randint(10,990)],
    [random.randint(10,990),random.randint(10,990),random.randint(10,990),random.randint(10,990)],
    [random.randint(10,990),random.randint(10,990),random.randint(10,990),random.randint(10,990)]]
line = [250,250, 1000,0]

def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  
def callback(event):
    global line, canvas, iterations
    line[0] = event.x
    line[1] = event.y
    line[2] = event.x + 1000
    line[3] = event.y
    canvas.delete("all")
    draw_frame()
def rotate_line(line):
    global angle
    a = angle
    y = line[3]
    x = line[2]
    new_x = - y*math.sin(a) + x*math.cos(a)
    new_y = y*math.cos(a) + x*math.sin(a)
    line[2] = new_x
    line[3] = new_y
    return line
def intercept(line,wall):
    x1 = wall[0]
    y1 = wall[1]
    x2 = wall[2]
    y2 = wall[3]
    x3 = line[0]
    y3 = line[1]
    x4 = line[2]
    y4 = line[3]
    den = (x1 - x2) * (y3-y4) - (y1-y2) * (x3-x4)
    if den==0:
        return False
    t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)) / den
    u = -((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3)) / den
    if (t>0 and t < 1 and u>0 and u<1):
        x = x1 + t * (x2-x1)
        y = y1 + t * (y2-y1)
        return [x,y]
    else:
        return False
def draw_frame():
    global line, wall, linewidth
    for i in range(len(wall)):
        canvas.create_line(wall[i][0],wall[i][1],wall[i][2],wall[i][3], width = linewidth)
    for q in range(iterations):
        intercept_location = []
        for i in range(len(wall)):
            intercepts = intercept(wall[i],line)
            if intercepts != False:
                intercept_location.append(intercepts)
        distances = []
        if len(intercept_location) > 1:
            for z in intercept_location:
                distances.append(calculateDistance(line[0],line[1],z[0],z[1]))
            interception = intercept_location[distances.index(min(distances))]
            canvas.create_line(line[0],line[1], interception[0], interception[1],fill=color)
        elif len(intercept_location) == 1:
            canvas.create_line(line[0],line[1], intercept_location[0][0], intercept_location[0][1],fill=color)
        window.update()
        line = rotate_line(line)

line = [250,250, 1000,0]
canvas.bind("<Button-1>",callback)
window.mainloop()