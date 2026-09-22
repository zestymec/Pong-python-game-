from turtle import Screen, Turtle
from paddle import paddle
Screen = Screen()
Screen.bgcolor("black")
Screen.setup(800, 600)
Screen.title("Pong")
Screen.tracer(0)


l_paddel = paddle((-350 , 0) ,  "W" , "S")
r_paddel = paddle((350 , 0) ,  "Up" , "Down")


Screen.exitonclick()
