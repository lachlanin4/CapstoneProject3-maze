import turtle as t

t.Turtle().screen.title('Turtle Escape')
t.Turtle().screen.bgcolor('#add8e6')

#turtle that will draw maze
maze_turtle = t.Turtle()
maze_turtle.pensize(4)

#Creates a square
for i in range (4):
  
  maze_turtle.fd(300)
  maze_turtle.left(90)

maze_turtle.goto
sophia = t.Turtle()
sophia.color('pink')
sophia.shape('turtle')
sophia.fd(30)


"""
#Movement functions in turtle
sophia.position() #shorthand:.pos
sophia.forward(25) #also accepts negative parameters
#forward can be shortened to sophia.fd
sophia.backward(90) #shorthand: .back and .bk
sophia.right(90) #rotates clockwise. parameter angle in degrees shorthand: .rt
sophia.left(180) #shorthand:.lt
sophia.heading() #find out angle turtle is heading
sophia.goto(30.50) #tells turtle where to go x,y parameters
sophia.setposition(600,90) #sets turtle position, xy parameters shorthand:setpos
sophia.setx()#just sets x coordinate leaves y unchanged
sophia.sety()#sets y coordinate
sophia.setheading()#sets angle turtle will face shorthand:.seth
sophia.home()#returns turtle to 0,0 coordinates and it's starting angle
sophia.dot(10,'green') #puts a dot on screen where turtle is, parameters are size and colour
sophia.fd(100);sophia.dot(20,'blue');sophia.fd(100) #You cannot draw with dot it is just a dot
#didn't know that you could use semi colons in python like this?

#Making a stamp, stamps leave a print of your shape in the place your turtle is
#If you make it as a variable you can use .clearstamp(variableName) to delete it
stampy =sophia.stamp()
sophia.fd(50)
sophia.clearstamp(stampy)

.clearstamps() to delete all stamps
sophia.hideturtle() short: ht()
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

# sophia.penup()
# sophia.goto(-160, 100)
# sophia.pendown()

# from random import randint

# for movement in range(100):
#   sophia.forward(randint(1,5))
#   josh.forward(randint(1,5))
#   damini.forward(randint(1,5))
#   holly.forward(randint(1,5))


t.mainloop()