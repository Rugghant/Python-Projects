from turtle import Turtle
import random

COLOR_LIST = ["light blue", "royal blue", "light steel blue",
              "steel blue", "light cyan", "light sky blue", "violet",
              "salmon", "red", "sandy brown", "purple", "deep pink",
              "deep pink", "medium sea green", "tomato"
              ]
WEIGHTS = [1, 2, 1, 1, 3, 2, 1, 4, 1, 3, 1, 1, 1,
           4, 1, 3, 2, 2, 1, 2, 1, 2, 1, 2, 1
           ]

class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.goto(x_cor, y_cor)
        self.color(random.choice(COLOR_LIST))
        self.quantity = random.choice(WEIGHTS)

        # defining borders of the brick
        self.r_wall = self.xcor() + 30
        self.l_wall = self.xcor() - 30
        self.upper_wall = self.ycor() + 15
        self.lower_wall = self.ycor() - 15


class Bricks:
    def __init__(self):
        self.y_start = 0
        self.y_end = 240
        self.bricks = []
        self.create_all_lanes()

    def create_lane(self, y_cor):
        for i in range(-580, 580, 63):
            brick = Brick(i, y_cor)
            self.bricks.append(brick)

    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 32):
            self.create_lane(i)


