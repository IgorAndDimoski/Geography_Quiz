from turtle import Turtle

class StateName(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state_name(self, name):
        self.write(name, align="center", font=("Arial", 8, "normal"))
        # self.goto(x,y)


    def move(self,x,y):
        self.goto(x,y)