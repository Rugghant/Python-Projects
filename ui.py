from turtle import Turtle
import random
import time

FONT1 = ("Courier", 52, "normal")
FONT2 = ("Courier", 32, "normal")
ALIGNMENT = "center"
COLOR = "white"
COLOR_LIST = ["light blue", "royal blue", "light steel blue",
              "steel blue", "light cyan", "light sky blue", "violet",
              "salmon", "red", "sandy brown", "purple", "deep pink",
              "deep pink", "medium sea green", "tomato"
              ]

class Ui(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(random.choice(COLOR_LIST))
        self.header()

    def header(self):
        self.clear()
        self.goto(0, -150)
        self.write("BREAKOUT", align=ALIGNMENT, font=FONT1)
        self.goto(0, -180)
        self.write("Press Space to START or RESUME the Game",
                   align=ALIGNMENT,
                   font=FONT2)

    def change_color(self):
        self.clear()
        self.color(random.choice(COLOR_LIST))
        self.header()

    def paused_state(self):
        self.clear()
        self.change_color()
        time.sleep(0.5)

    def game_over(self, win):
        self.clear()
        if win == True:
            self.write("you won!", align=ALIGNMENT, font=FONT1)
        else:
            self.write("Game is over...", align=ALIGNMENT, font=FONT1)




