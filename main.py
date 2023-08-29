import turtle, time, random
from turtle import *

turtle.showturtle()
def ahead():
  turtle.forward(100)
def behind():
  turtle.backward(100)
def clockwise():
  turtle.right(100)
def counterclockwise():
  turtle.left(100)
def hide():
	i = 0
	while i >= 0:
		i+=1
		turtle.isvisible()
		time.sleep
def peen():
	if turtle.isdown() == False:
		turtle.pendown()
	else:
		turtle.penup()
#def penUp():
#	turtle.penup()
#def penDown():
#	turtle.pendown()
def clear():
	turtle.clear()

def changeColor():
	r = random.uniform(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	turtle.pencolor(r, g, b)

def shoot():
	bullet = Turtle()
	bullet.hideturtle()
	bullet.penup()
	#bullet.goto(50, 50)
	x = turtle.xcor()
	y = turtle.ycor()
	bullet.goto(x,y)
	bullet.setheading(turtle.heading())
	bullet.showturtle()
	bullet.forward(200)
	bullet.reset()


turtle.Screen().onkey(shoot, "Q")
turtle.Screen().onkey(changeColor, "E")
turtle.Screen().onkey(ahead, "W")
turtle.Screen().onkey(behind, "S")
turtle.Screen().onkey(clockwise, "D")
turtle.Screen().onkey(counterclockwise, "A")
turtle.Screen().onkey(peen, "Space")
#turtle.Screen().onkey(peen, "Shift")
turtle.Screen().listen()
turtle.Screen().onkey(clear, "R")

#use threading
#deleate or hide bullet
#goto turtle and change direction