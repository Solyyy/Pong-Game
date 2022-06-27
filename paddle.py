from turtle import Turtle

HEIGHT = 5
WIDTH = 1

UP = 0
DOWN = 180
STEP = 20

BORDER = 280
COLOR = "white"


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(COLOR)
        self.setheading(90)
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + STEP
        if self.ycor() < 240:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - STEP
        if self.ycor() > -240:
            self.goto(self.xcor(), new_y)


