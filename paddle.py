import turtle
class Paddle(turtle.Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(pos)

    def go_up(self):
        newy=self.ycor() + 20
        self.goto(self.xcor(), newy)
    def go_down(self):
        newy=self.ycor() - 20
        self.goto(self.xcor(), newy)

