from turtle import Turtle


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.setposition(position)
        self.color("white")
        self.x_mov = 10
        self.y_mov = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_mov
        new_y = self.ycor() + self.y_mov
        self.goto(new_x, new_y)

    def x_bounce(self):
        self.x_mov *= -1

    def y_bounce(self):
        self.y_mov *= -1

    def reset(self):
        self.goto(0, -257)
        self.y_bounce()