import turtle
import paddle
import ball
import time
import scoreboard

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))
ball=ball.ball_paddle()
scoreboard=scoreboard.Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #ball detection on top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce
        ball.bounce_y()
    #detect collision ball with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect when right paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    #detect when left paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()