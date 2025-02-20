from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setposition(position)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")

    def go_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())

    def reset(self):
        self.goto(0, -280)