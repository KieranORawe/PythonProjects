from tkinter import *
import math

window = Tk()
canvas = Canvas(window, width=500,height=500, background="white")
canvas.pack()

def intercept(line,wall):
    x1 = wall[0][0]
    y1 = wall[0][1]
    x2 = wall[1][0]
    y2 = wall[1][1]

    x3 = line[0][0]
    y3 = line[0][1]
    x4 = line[1][0]
    y4 = line[1][1]

    den = (x1 - x2) * (y3-y4) - (y1-y2) * (x3-x4)

    if den==0:
        return False
    t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)) / den
    u = -((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3)) / den
    

    if t>0 and t < 1 and u>0:
        x = x1 + t * (x2-x1)
        y = y1 + t * (y2-y1)
        return [x,y]
    else:
        return False
def rotate_line(line,angle):
    x = line[1][0] 
    y = line[1][1]
    print(x)
    print(y)
    new_x = x*math.cos(math.radians(angle))-y*math.sin(math.radians(angle))
    new_y = x*math.sin(math.radians(angle))+y*math.cos(math.radians(angle))
    line[1][0] = new_x
    line[1][1] = new_y
    return line

walls = [ 
          [[75,90],[100,490]],
          [[10,10],[490,10]],
          [[490,10],[490,490]],
          [[490,490],[10,490]],
          [[10,490],[10,10]],
        ]
line = [[250,250],[10000,250]]

for i in range(72):
    for i in walls:
        canvas.create_line(i[0][0], i[0][1], i[1][0], i[1][1])
        intercept_location = intercept(i,line)
        if intercept_location != False:
            canvas.create_line(line[0][0],line[0][1],intercept_location[0],intercept_location[1])
    line = rotate_line(line,5)
window.mainloop()