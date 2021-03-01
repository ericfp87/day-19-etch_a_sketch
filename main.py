from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")

def forwarding():
    tim.forward(10)

def lefting():
    tim.left(10)

def righting():
    tim.right(10)

def backing():
    tim.back(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkeypress(forwarding, "w")
screen.onkeypress(lefting, "a")
screen.onkeypress(righting, "d")
screen.onkeypress(backing, "s")
screen.onkey(clear, "c")
screen.listen()

screen.exitonclick()

