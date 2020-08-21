from __future__ import division 
from tkinter import *
import math
import random
import time
import shapely
from shapely.geometry import LineString, Point

def Locate(A,B,C,D):
    line1 = LineString([A, B])
    line2 = LineString([C, D])

    int_pt = line1.intersection(line2)
    try:
        point_of_intersection = int_pt.x, int_pt.y
        return point_of_intersection
    except:
        return 0,0


window = Tk()

canvas = Canvas(window, width=500,height=500, background="white")
canvas.pack()

angle = 0
distance = 5

lines = [ 
          [[250,250],[260,250]],  
          [[10,10],[490,10]],
          [[490,10],[490,490]],
          [[490,490],[10,490]],
          [[10,490],[10,10]],
          [[75,90],[120,85]]
        ]
for i in lines:
    canvas.create_line(i[0][0], i[0][1], i[1][0], i[1][1])

for i in range(10):
    change_in_x = random.randint(-1,1)
    change_in_y = random.randint(-1,1)
    
    lines[0][0][0] += change_in_x
    lines[0][1][0] += change_in_x

    lines[0][0][1] += change_in_y
    lines[0][1][1] += change_in_y

    for i in range(10):
        distances = []
        for q in range(1,len(lines)):
            R = Locate(lines[0][0],lines[0][1],lines[q][0],lines[q][1])
            if not R:
                pass
            else:
                distances.append(R)
        angle = angle+20
        lines[0][1][0] = lines[0][1][0]+100*math.cos(angle)
        lines[0][1][1] = lines[0][1][1]+100*math.sin(angle)
        dist = []
        for z in distances:
            dist.append(math.sqrt(((lines[0][0][0]-z[0])*(lines[0][0][0]-z[0]))+((lines[0][0][1]-z[1])*(lines[0][0][1]-z[1]))))
        index = dist.index(min(dist))
        canvas.create_line(lines[0][0][0],lines[0][0][1],distances[index][0],distances[index][1])
    canvas.update()
    time.sleep(1)
    canvas.delete("all")
    for i in lines:
        canvas.create_line(i[0][0], i[0][1], i[1][0], i[1][1])
print("done")
window.mainloop()
