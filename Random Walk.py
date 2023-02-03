import random
import turtle
from turtle import Turtle, Screen, colormode
from random import randint

turtle.colormode(255)
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("arrow")
timmy_the_turtle.speed(10)
timmy_the_turtle.pensize(10)

direction_list = [0, 90, 180, 270]

def random_color_generator():
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    random_color = r, g, b
    return (random_color)


for i in range(1000000):
    timmy_the_turtle.forward(20)
    timmy_the_turtle.setheading(random.choice(direction_list))
    timmy_the_turtle.color(random_color_generator())

screen = Screen()
timmy_the_turtle.pencolor(random_color_generator())
screen.exitonclick()