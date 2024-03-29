import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S. States Game')

img = 'blank_states_img.gif'
turtle.addshape(img)
turtle.shape(img)

# Extract states into a list
data = pandas.read_csv('./50_states.csv')
all_states_data = data['state']
states_data_list = all_states_data.to_list()

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

num_states = 50
score = 0
states_guessed = []

while len(states_guessed) < num_states:
    # Get input from user and capitalize
    answer = screen.textinput(title=f'{score}/{num_states} States Correct', prompt='What\'s another state\'s name?')
    answer = answer.title()

    if answer == 'Exit':
        break

    # pull the x and y coordinates of the state and write to the map
    # is_in_list = answer in states_data_list
    if answer in states_data_list:
        state_info = data[data['state'] == answer]
        x_cor = int(state_info['x'])
        y_cor = int(state_info['y'])
        tim.goto(x_cor, y_cor)
        state_name = state_info['state'].item()
        # print(state_name)
        tim.write(arg=state_name, align='center', font=('Courier', 8, 'normal'))
        states_guessed.append(answer)
        score += 1

# create csv file of missed states
# missed_states = []
# for state in all_states_data:
#     if state not in states_guessed:
#         missed_states.append(state)

missed_states = [state for state in all_states_data if state not in states_guessed]

missed_states_data_frame = pandas.DataFrame(missed_states)
missed_states_data_frame.to_csv('./missed_states.csv')

# screen.exitonclick()
# turtle.mainloop()
