import turtle
import pandas as pd

class StateTurtle(turtle.Turtle):
    def __init__(self, state_name, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(state_name, align="center", font=("Arial", 8, "normal"))

class USStatesQuiz:
    def __init__(self):
        # Set up the screen
        self.screen = turtle.Screen()
        self.screen.title("U.S. States Game")
        self.image = "blank_states_img.gif"
        self.screen.addshape(self.image)
        turtle.shape(self.image)

        # Load state data
        self.data = pd.read_csv("50_states.csv")
        self.all_states = self.data.state.to_list()
        self.guessed_states = []

    def start(self):
        while len(self.guessed_states) < 50:
            answer_state = self.screen.textinput(
                title=f"{len(self.guessed_states)}/50 States Correct",
                prompt="What's another state's name?"
            ).title()

            if answer_state == "Exit":
                self.save_missing_states()
                break

            if answer_state in self.all_states and answer_state not in self.guessed_states:
                self.guessed_states.append(answer_state)
                state_data = self.data[self.data.state == answer_state]
                state_turtle = StateTurtle(answer_state, int(state_data.x), int(state_data.y))


    def save_missing_states(self):
        missing_states = [state for state in self.all_states if state not in self.guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")


game = USStatesQuiz()
game.start()
