import turtle
import pandas
from state import StateName

data = pandas.read_csv("50_states.csv")
list_states = data.state.values.tolist()

screen = turtle.Screen()
turtle.addshape("blank_states_img.gif")
image = "blank_states_img.gif"
turtle.shape(image)
guessed_states = []

while len(guessed_states) < 50:
    user_guess = screen.textinput(
                title=f"{len(guessed_states)}/50 States Correct",
                prompt="What's another state's name?").title()
    if user_guess == "Exit":
        missing_states = [i for i in list_states if i not in guessed_states]
        print(f'Here are the states names that you are missing : {missing_states}')
        print(f"In totall you are missing {len(missing_states)}")
        missing_states = [state for state in list_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        # pandas.DataFrame(missing_states).to_csv("../New folder/Missing_states.csv")
        break
    if user_guess in list_states:
        coordinate = data[data.state == user_guess]
        x = coordinate.x.item()
        y= coordinate.y.item()
        state_name = StateName()
        guessed_states.append(user_guess)
        state_name.move(x,y)
        state_name.write_state_name(name=user_guess, )



