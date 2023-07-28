import turtle as t
from turtle import Screen
import time

t.Turtle().screen.title('Turtle Escape')
t.Turtle().screen.bgcolor('#add8e6')
t.Turtle().hideturtle() #for some reason this does not hide the original turtle so change colour to blend with background
t.Turtle().color('#add8e6')

class Maze(t.Turtle):
  def __init__(self,turtle):
    self.width = None
    self.height = None
    self.drawer = turtle


  def createOutline(self,drawer):
    for i in range (4):
      drawer.up()
      drawer.fd(30)
      drawer.down()
      drawer.fd(150)
      drawer.left(90)
    
  def 
#turtle that will draw maze
maze_turtle = t.Turtle()
maze_turtle.pensize(4)
maze_turtle.color('blue')
maze_turtle.pen(speed=10)

#The below maze is a 180x180 maze with pathways of 30 width
#Creates a square, basic outline of maze
# for i in range (4):
#   maze_turtle.up()
#   maze_turtle.fd(30)
#   maze_turtle.down()
#   maze_turtle.fd(150)
#   maze_turtle.left(90)
maze1 = Maze(maze_turtle)
maze1.createOutline(maze_turtle)

#Made some functions to help draw because I got tired
#in this mode the angles are 0 - east, 90 - north, 180-west,270-south
def drawLeft():
  maze_turtle.down()
  maze_turtle.setheading(180)
  maze_turtle.fd(30)

def drawRight():
  maze_turtle.down()
  maze_turtle.seth(0)
  maze_turtle.fd(30)

def drawUp():
  maze_turtle.down()
  maze_turtle.seth(90)
  maze_turtle.fd(30)

def drawDown():
  maze_turtle.down()
  maze_turtle.seth(270)
  maze_turtle.fd(30)

def skipLine(angle):
  maze_turtle.up()
  maze_turtle.seth(angle)
  maze_turtle.fd(30)
  maze_turtle.down()
  

#drawing a maze
maze_turtle.up()
maze_turtle.goto(30,0);drawUp();drawRight();drawRight();skipLine(0)
drawDown();drawRight();drawRight();drawUp();drawLeft();drawUp()
drawLeft();skipLine(180);drawLeft();drawLeft();drawUp();drawRight()
drawRight();drawRight();drawRight();skipLine(0);drawUp();drawLeft()
skipLine(180);drawLeft();drawLeft();skipLine(180);drawLeft();drawUp()
drawUp();drawRight();drawDown();drawRight();drawRight();skipLine(0)
drawRight();drawRight()

maze_turtle.ht() #hiding the turtle that drew it

#starting and ending points to the maze
maze1EntryPoint = (15.00,0.00)
maze1ExitPoint = (165.00,180.00)


def playerUp():
  player.seth(90)
  player.fd(15)
  if player.position()==maze1ExitPoint:
    print("You have won!")
  time.sleep(0.5)

def playerDown():
  player.seth(270)
  player.fd(15)
  if player.position()==maze1ExitPoint:
    print("You have won!")
  time.sleep(0.5)

def playerLeft():
  player.seth(180)
  player.fd(15)
  if player.position()==maze1ExitPoint:
    print("You have won!")
  time.sleep(0.5)

def playerRight():
  player.seth(0)
  player.fd(15)
  if player.position()==maze1ExitPoint:
    print("You have won!")
  time.sleep(0.5)

Screen().onkey(playerUp,'Up')
Screen().onkey(playerLeft,'Left')
Screen().onkey(playerRight,'Right')
Screen().onkey(playerDown,'Down')
Screen().listen()

player = t.Turtle()
player.color('pink')
player.shape('turtle')
player.up()
player.goto(15,0)
player.seth(90)
player.down()

print(player.position())
#while True:

  # else:
  #   print("Still going") #Creates an error
"""
#Movement functions in turtle
player.position() #shorthand:.pos
player.forward(25) #also accepts negative parameters
#forward can be shortened to player.fd
player.backward(90) #shorthand: .back and .bk
player.right(90) #rotates clockwise. parameter angle in degrees shorthand: .rt
player.left(180) #shorthand:.lt
player.heading() #find out angle turtle is heading
player.goto(30.50) #tells turtle where to go x,y parameters
player.setposition(600,90) #sets turtle position, xy parameters shorthand:setpos
player.setx()#just sets x coordinate leaves y unchanged
player.sety()#sets y coordinate
player.setheading()#sets angle turtle will face shorthand:.seth
player.home()#returns turtle to 0,0 coordinates and it's starting angle
player.dot(10,'green') #puts a dot on screen where turtle is, parameters are size and colour
player.fd(100);player.dot(20,'blue');player.fd(100) #You cannot draw with dot it is just a dot
#didn't know that you could use semi colons in python like this?

#Making a stamp, stamps leave a print of your shape in the place your turtle is
#If you make it as a variable you can use .clearstamp(variableName) to delete it
stampy =player.stamp()
player.fd(50)
player.clearstamp(stampy)

.clearstamps() to delete all stamps
player.hideturtle() short: ht()
.showturtle() .st()

.pensize parameter is width
"""
# s = t.Shape("compound")
# poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
# s.addcomponent(poly1, "red", "blue")
# poly2 = ((0,0),(10,-5),(-10,-5))
# s.addcomponent(poly2, "blue", "red")
# t.register_shape("myshape", s)
# t.shape("myshape")

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         t.color(c)
#         t.forward(steps)
#         t.right(30)
# t.color('red')
# t.fillcolor('yellow')
# t.begin_fill()
# while True:
#     t.forward(200)
#     t.left(170)
#     if abs(t.pos()) < 1:
#         break
# t.end_fill()

# player.penup()
# player.goto(-160, 100)
# player.pendown()

# from random import randint

# for movement in range(100):
#   player.forward(randint(1,5))
#   josh.forward(randint(1,5))
#   damini.forward(randint(1,5))
#   holly.forward(randint(1,5))


t.mainloop()