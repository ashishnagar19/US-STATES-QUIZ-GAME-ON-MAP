import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:

        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 US STATES GAME",
                                prompt="What's another states name?").title()

        if answer_state == "Exit":
            missing_states = [state for state in all_states if state not in guessed_states]
            new_data = pd.DataFrame(missing_states)
            new_data.to_csv("missing_states.csv")
            break



        if answer_state in all_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            states_data = data[data.state == answer_state]
            t.goto(int(states_data.x), int(states_data.y))
            t.write(answer_state)






screen.exitonclick()

