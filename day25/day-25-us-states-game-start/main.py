from turtle import Turtle, Screen, hideturtle
from numpy import size
import pandas


data_set = pandas.read_csv(
    "day25/day-25-us-states-game-start/50_states.csv", index_col=False
)
states_data_set = data_set.state.to_list()
x_cor = data_set.x.to_list()
y_cor = data_set.y.to_list()
scrn = Screen()
scrn.setup(725, 491)
scrn.title("Guess U.S. States")
scrn.bgpic("day25/day-25-us-states-game-start/blank_states_img.gif")
is_game_on = True
correct_answ = 0
while is_game_on:
    user_input = str(scrn.textinput(title=f"Correct {correct_answ}/{len(states_data_set)}", prompt="What's next state?"))
    if user_input.title() in states_data_set:
        index = states_data_set.index(user_input.title())
        for i in range(0, len(states_data_set)):
            print(states_data_set[index])
            state = Turtle()
            state.hideturtle()
            state.up()
            state.goto(x_cor[index], y_cor[index])
            state.write(
                align="center", arg=states_data_set[index], font=("Arial", 10, "normal")
            )
            correct_answ += 1 
            break
    else:
        disp = Turtle()
        disp.hideturtle()
        disp.write(align="center",arg=f"GAME OVER \nYour score: {correct_answ}", font=("Arial", 20, "normal"))
        break

scrn.exitonclick()

# states = pandas.read_csv("day25/day-25-us-states-game-start/50_states.csv")
