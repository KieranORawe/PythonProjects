
#origin = [0,0]
#Vector = [1,1]
#def VectorToCords(origin, Vector):
#    return origin[0]+Vector[0],origin[1]+Vector[1]

from tkinter import *
import math

window = Tk()
canvas = Canvas(window, width=1000,height=1000, background="white")
canvas.pack()


x = 0
y = math.sin(math.radians(x))
previous = [x,(y*400)+500]
for i in range(0,1000,1):
    x = i
    y = math.sin(math.radians(x))
    canvas.create_line(previous,x,(y*400)+500)
    previous = [x,(y*400)+500]
window.mainloop()