#PythonDraw.py
import turtle
turtle.setup(650,350,200,200)#the location and size of frame,startXY width height
turtle.penup()#no draw
turtle.fd(-250)#back 250
turtle.pendown()#start draw
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)#absolute angle
for i in range(4):
    turtle.circle(40,80)#turn left,r=40,angle=80
    turtle.circle(-40,80)
turtle.circle(-40,80/2)
turtle.fd(40)
turtle.cilce(16,180)
turtle.fd(40*2/3)
turtle.down()#