from turtle import *
import time


def safeDrawing():
    hideturtle()
    setup(1.0, 1.0)
    fillcolor('#9da8a0') 
  
    begin_fill() 
    bgcolor('light blue')
    speed(10)
    penup()
    backward(150)
    left(90)
    forward(150)
    right(90)
    pendown()


    for i in range(4):
        forward(300)
        right(90)
    end_fill() 

    penup()
    forward(10)
    right(90)
    forward(10)
    left(90)
    pendown()

    for i in range(4):
        forward(280)
        right(90)




    penup()
    forward(90)
    right(90)
    forward(140)
    pendown()

    fillcolor('#686e6a')
    begin_fill()
    r = 50
    circle(r)
    end_fill()

    penup()
    left(90)
    forward(20)
    right(90)

    pendown()

    fillcolor('#bec4c0')
    begin_fill()
    r = 30
    circle(r)
    end_fill()

    penup()
    left(90)
    forward(30)
    pendown()

    speed(20)
    for i in range(4):
        forward(80)
        right(90)
        forward(2.5)
        fillcolor('white')
        begin_fill()
        circle(6)
        end_fill()
        forward(2.5)
        right(90)
        forward(80)
        right(90)
    speed(10)
    time.sleep(2)
    clear()
    textDrawing()

def textDrawing():
    setup(1.0, 1.0)
    style1 = ('Arial', 80, 'bold')
    style2 = ('Arial', 20, 'italic')
    style3 = ('Arial', 30, 'italic')
    bgcolor('black')
    color('red')
    write("HACK THE SAFE\n", font=style1, align='center')
    write("A Terrifying Net Force \n        Production\n\n", font=style2, align='center')


    speed(5)
    penup()
    right(90)
    forward(50)
    left(90)
    left(180)
    forward(600)
    left(180)
    pendown()
    fillcolor('black')
    speed(4)
    begin_fill()
    for i in range(2):
        forward(1200)
        left(90)
        forward(400)
        left(90)
    end_fill()
    penup()
    speed(30)
    forward(600)
    left(90)
    forward(200)
    write("Click anywhere to proceed", font=style3, align="center")

    



    exitonclick()



