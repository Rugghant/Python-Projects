from turtle import Turtle

try:
    score = open("highestScore.txt", "r").read()
except FileNotFoundError:
    score = open("highestScore.txt", "w").write(str(0))
except ValueError:
    score = 0

FONT = ("arial", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self, lives):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = lives
        self.highscore = score
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto((-580, 260))
        self.write(f"Score: {self.score}   Highest Score: {self.highscore}",
                   align="left",
                   font=FONT)
        self.goto((580, 260))
        self.write(f"Lives : {self.lives}", align="right", font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
        self.update_score()

    def decrease_lives(self):
        self.lives -= 1
        self.update_score()

    def reset(self):
        self.clear()
        self.score = 0
        self.update_score()
        open("highestScore.txt", "w"). write(str(self.highscore))
