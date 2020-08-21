import math
import turtle

start_x = 0
start_y = 200

frame = turtle.Turtle()

frame.up()
frame.goto(start_x,start_y)
frame.down()

frame.begin_fill()
frame.goto(start_x-10,start_y+0)
frame.goto(start_x-10,start_y+10)
frame.goto(start_x+10,start_y+10)
frame.goto(start_x+10,start_y+0)
frame.goto(start_x+0,start_y+0)
frame.end_fill()
frame.hideturtle()

turtle.right(90)
turtle.tracer(0)
t = 0
starting_angle = 45

medium = turtle.Turtle()
long = turtle.Turtle()

short_l = 300
medium_l = 200
long_l = 100


turtle.goto(start_x,start_y)

turtle.pencolor("red")
medium.pencolor("orange")
long.pencolor("green")

turtle.fillcolor("red")
medium.fillcolor("orange")
long.fillcolor("green")

turtle.hideturtle()
medium.hideturtle()
long.hideturtle()

turtle.shape("circle")
medium.shape("circle")
long.shape("circle")


def angle(time, L):
    global starting_angle
    return starting_angle*math.cos(    math.sqrt(9.8/L)    *time)

while True:
    turtle.clear()
    medium.clear()
    long.clear()


    
    turtle.setheading(270)
    turtle.left(angle(t, short_l/10))
    turtle.fd(short_l)
    turtle.stamp()

    medium.goto(turtle.pos())
    medium.setheading(270)
    medium.left(angle(t, medium_l/10)+angle(t, short_l/10))
    medium.fd(medium_l)
    medium.stamp()

    long.goto(medium.pos())
    long.setheading(270)
    long.left(angle(t, long_l/10)+angle(t, medium_l/10)+angle(t, short_l/10))
    long.fd(long_l)
    long.stamp()
    long.bk(long_l)
    
    medium.bk(medium_l)
    
    turtle.bk(short_l)

    
    t += 0.005
    turtle.update()
