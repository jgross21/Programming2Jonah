# Functions can call functions

def f():
    print('f')
    g()

def g():
    print('g')

f()

# Function calling itself
def f():
    print('f')
    f()
#f()

# we can controll the recursion depth
def controlled(level, end_level):
    print('Recursion level:', level)
    if level < end_level:
        controlled(level + 1, end_level)

controlled(0, 10)

import turtle
import random

my_turtle = turtle.Turtle()
my_turtle.speed(8)
my_turtle.width(3)
my_turtle.shape('turtle')
my_screen = turtle.Screen()

'''
my_turtle.goto(0, 0)
my_turtle.goto(100, 0)
my_turtle.goto(100, 100)

my_turtle.pencolor('lightblue')
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(45)
my_turtle.backward(50)

my_turtle.penup()
my_turtle.goto(0, 0)
my_turtle.pendown()

my_turtle.setheading(90) # turn to the heading (0 right, 90 up, 180 left)

# draw a shape
my_turtle.fillcolor('red')
my_turtle.pencolor('black')

my_turtle.begin_fill()

for i in range(8):
    my_turtle.forward(50)
    my_turtle.right(360 / 8)

my_turtle.end_fill()

distance = 20
for i in range (100):
    my_turtle.forward(distance + i)
    my_turtle.right(15)
my_screen.clear()
'''

def rect(width, heihgt):
    my_turtle.penup()
    my_turtle.goto(-width / 2,  heihgt / 2)
    my_turtle.pendown()
    my_turtle.pencolor('purple')
    my_turtle.setheading(0)
    for i in range(2):
        my_turtle.forward(width)
        my_turtle.right(90)
        my_turtle.forward(heihgt)
        my_turtle.right(90)

def rectcursive(width, heihgt, depth ,linewidth=3):
    if depth > 0:
        my_turtle.pensize(linewidth)
        my_turtle.penup()
        my_turtle.goto(-width / 2,  heihgt / 2)
        my_turtle.pendown()
        my_turtle.pencolor('purple')
        my_turtle.setheading(0)
        for i in range(2):
            my_turtle.forward(width)
            my_turtle.right(90)
            my_turtle.forward(heihgt)
            my_turtle.right(90)
        rectcursive(width * 1.25, heihgt * 1.25, depth - 1, linewidth * 1.25)

#rectcursive(40, 15, 12, 1)

def bracket_recursion(size, depth, x=-300, y=0):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.forward(100)# makes constant
    pos1 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(270)
    my_turtle.forward(size)
    my_turtle.left(90)
    my_turtle.forward(100)
    pos2 = my_turtle.pos()

    if depth > 0:
        x, y = pos1
        bracket_recursion(size * .5, depth - 1, x, y)
        x, y = pos2
        bracket_recursion(size * .5, depth - 1, x, y)

bracket_recursion(100, 5)

my_screen.exitonclick()
