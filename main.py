from turtle import Screen, Turtle
from paddle import Paddle

Screen = Screen()
Screen.bgcolor("black")
Screen.setup(800, 600)
Screen.title("Pong")
Screen.tracer(0)


l_paddel = Paddle((-350, 0))
r_paddel = Paddle((350, 0))

Screen.listen()
Screen.onkey(r_paddel.go_up, "UP")
Screen.onkey(r_paddel.go_down, "Down")
Screen.onkey(l_paddel.go_up, "w")
Screen.onkey(l_paddel.go_down, "s")

game_is_on = True
while game_is_on:
    Screen.update()

Screen.exitonclick()
