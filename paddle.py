from turtle import screen , Turtle

class Paddle(Turtle):
    def __init__(self):
            super().__init__()
            paddle = Turtle()
            paddle.shape("square")
            paddle.color("white")
            paddle.shapesize(5 , 1)
            paddle.penup()
            paddle.goto(350 , 0)



# Screen = screen()

# def paddle(position , btn1 , btn2):
#     paddle = Turtle()
#     paddle.shape("square")
#     paddle.color("white")
#     paddle.shapesize(stretch_wid=5, stretch_len=1)
#     paddle.penup()
#     paddle.goto(position)


#     def go_up():
#         new_y = paddle.ycor() + 20
#         paddle.goto(paddle.xcor(), new_y)


#     def go_down():
#         new_y = paddle.ycor() - 20
#         paddle.goto(paddle.xcor(), new_y)


#     Screen.listen()
#     Screen.onkey(go_up, btn1)
#     Screen.onkey(go_down, btn2)

#     game_is_on = True
#     while game_is_on:
#         Screen.update()