from turtle import Turtle

COLOR = "white"
WIDTH = 5


class GameBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(COLOR)
        self.setheading(90)
        self.pensize(WIDTH)
        self.penup()
        self.walk()

    def walk(self):
        self.goto(0, -340)
        self.pendown()
        for x in range(30):
            self.forward(20)
            self.pendown()
            self.forward(20)
            self.penup()


