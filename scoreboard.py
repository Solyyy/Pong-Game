from turtle import Turtle, Screen
screen = Screen()

ALIGNMENT = "center"
FONT = ('Arial', 40, 'normal')

class Scoreboard(Turtle):

    loc_l_scoreboard = -175, 240
    loc_r_scoreboard = 175, 240

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.create_scoreboard()

    def reset_scoreboard(self):
        self.clear()
        self.create_scoreboard()

    def add_score_l(self):
        self.l_score += 1
        self.reset_scoreboard()

    def add_score_r(self):
        self.r_score += 1
        self.reset_scoreboard()

    def create_scoreboard(self):
        self.goto(self.loc_l_scoreboard)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(self.loc_r_scoreboard)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

