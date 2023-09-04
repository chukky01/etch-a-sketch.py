#import turtle and screen
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

#define the movements
def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():#clears when you've made a mistake and want to go  back to the beginning
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
#Using an event listener
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")


#so that the screen does not go once it appears
screen.exitonclick()
