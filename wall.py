from turtle import Turtle


class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setposition(x_cor, y_cor)
        self.shapesize(stretch_wid=1, stretch_len=3)




