
#Turtle Recursion (25pts)
import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.width(3)
my_turtle.shape('turtle')
my_screen = turtle.Screen()

#1)  Using the turtle library, create the H fractal pattern according to the file shown in the data folder. (10pts)  
def h_fractal(size=100, depth=3, x=0, y=0):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(0)
    my_turtle.forward(size)
    my_turtle.left(90)
    my_turtle.forward(size)
    pos1 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(0)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.forward(size)
    pos2 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(180)
    my_turtle.forward(size)
    my_turtle.left(90)
    my_turtle.forward(size)
    pos3 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(180)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.forward(size)
    pos4 = my_turtle.pos()

    if depth > 0:
        x, y = pos1
        h_fractal(size * .5, depth - 1, x, y)
        x, y = pos2
        h_fractal(size * .5, depth - 1, x, y)
        x, y = pos3
        h_fractal(size * .5, depth - 1, x, y)
        x, y = pos4
        h_fractal(size * .5, depth - 1, x, y)

# h_fractal()

#2)  Using the turtle library, create any of the other recursive patterns in the data folder. 
#  Challenge yourself to match your pattern as closely as you can to the image.  (10pts)
#  Note:  The Koch snowflake shows step by step building of the fractal.  
#  The rectangle fractal example shows 4 possible drawings of the same fractal (choose any one)

def snowflake_fractal(size=200, depth=3, x=0, y=0):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(90)
    my_turtle.right(180/6)

    my_turtle.right(360 / 6)
    my_turtle.forward(size)
    mypos1 = my_turtle.pos()
    my_turtle.backward(size)

    my_turtle.right(360 / 6)
    my_turtle.forward(size)
    mypos2 = my_turtle.pos()
    my_turtle.backward(size)

    my_turtle.right(360 / 6)
    my_turtle.forward(size)
    mypos3 = my_turtle.pos()
    my_turtle.backward(size)

    my_turtle.right(360 / 6)
    my_turtle.forward(size)
    mypos4 = my_turtle.pos()
    my_turtle.backward(size)

    my_turtle.right(360 / 6)
    my_turtle.forward(size)
    mypos5 = my_turtle.pos()
    my_turtle.backward(size)

    my_turtle.right(360 / 6)
    my_turtle.forward(size)
    mypos6 = my_turtle.pos()
    my_turtle.backward(size)

    if depth > 0:
        x, y = mypos1
        snowflake_fractal(size * .3, depth - 1, x, y)

        x, y = mypos2
        snowflake_fractal(size * .3, depth - 1, x, y)

        x, y = mypos3
        snowflake_fractal(size * .3, depth - 1, x, y)

        x, y = mypos4
        snowflake_fractal(size * .3, depth - 1, x, y)

        x, y = mypos5
        snowflake_fractal(size * .3, depth - 1, x, y)

        x, y = mypos6
        snowflake_fractal(size * .3, depth - 1, x, y)

# snowflake_fractal()

#3)  Create your own work of recursive art with a repeating pattern of your making (or choose another one from the files).  
#  It must be a repeated pattern using recursion (not just loops). Snowflakes, trees, and spirals are a common choice.  
#  Play around and have fun with it.  (5pt) 

# Open-sided serpinski
def my_fractal(size=200, depth=3, x=-100, y=-100):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(90)
    my_turtle.right(90)

    my_turtle.forward(size)
    pos1 = my_turtle.pos()
    my_turtle.left(120)

    my_turtle.forward(size)
    pos2 = my_turtle.pos()
    my_turtle.left(120)

    my_turtle.forward(size)
    pos3 = my_turtle.pos()
    my_turtle.left(120)

    if depth > 0:
        x, y = pos3
        my_fractal(size * .5, depth - 1, x, y)

        x, y = pos1
        my_fractal(size * .5, depth - 1, x, y)

        x, y = pos2
        my_fractal(size * .5, depth - 1, x, y)


my_fractal()


#  General expectations for all problems
#  Give all your fractals a depth of at least 4.  (Don't make programs that take forever though)  
#  Ensure the recursive drawing is contained on the screen (at whatever size you set it).
#  All three recursive drawings can be on the same program.  Just use screen.clear() between problems.  Alternately, you could draw to three different screen objects.
#  Run your turtles at max speed.
#  Have fun!
 
#  Resource to help you out >>> https://docs.python.org/3.3/library/turtle

my_screen.exitonclick()
