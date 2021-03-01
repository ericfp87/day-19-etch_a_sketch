from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")

def forwarding():
    tim.forward(10)

def lefting():
    tim.left(1)

def righting():
    tim.right(1)

def backing():
    tim.back(10)


screen.onkeypress(forwarding, "w")
screen.onkeypress(lefting, "a")
screen.onkeypress(righting, "d")
screen.onkeypress(backing, "s")
screen.listen()

screen.exitonclick()

