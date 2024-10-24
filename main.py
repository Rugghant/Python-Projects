from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from bricks import Bricks
from ui import Ui

screen = Screen()
screen.title("Welcome to the BreakOut Game!")
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.tracer(0)

ui = Ui()
ui.header()
paddle = Paddle((0, -280))
ball = Ball((0, -257))
brick_wall = Bricks()
score_board = Scoreboard(5)
# brick1 = Brick(x_cor=-560, y_cor=20).color("red")
# brick2 = Brick(x_cor=-560, y_cor=40).color("orange")
# brick3 = Brick(x_cor=-560, y_cor=60).color("pink")
# brick4 = Brick(x_cor=-560, y_cor=80).color("yellow")

game_pause = False
game_on = True


def pause_game():
    global game_pause
    if game_pause:
        game_pause = False
    else:
        game_pause = True


screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")
screen.onkey(pause_game, "space")


while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collisions with walls and bounce
    if ball.ycor() > 280:
        ball.y_bounce()

    if ball.xcor() > 580 or ball.xcor() < -580:
        ball.x_bounce()

    # Detect collision with paddle and bounce
    if ball.distance(paddle) < 50:
        ball.y_bounce()

    # Detect paddle misses the ball
    if ball.ycor() < -280 and ball.ycor() > -300:
        score_board.decrease_lives()
        paddle.reset()
        ball.reset()
        if score_board.lives == 0:
            score_board.reset()
            game_on = False
            ui.game_over(win=False)
        ui.change_color()

    # Detect collision with bricks and bounce
    for brick in brick_wall.bricks:
        if ball.distance(brick) < 40:
            score_board.increase_score()
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000, 3000)
                brick_wall.bricks.remove(brick)

screen.exitonclick()

