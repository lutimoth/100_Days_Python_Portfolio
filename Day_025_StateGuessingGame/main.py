import turtle
import pandas as pd

states_info = pd.read_csv("50_states.csv")
all_states = states_info['state'].to_list()

screen = turtle.Screen()
screen.title("U.S. State Game")
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

# For getting mouse coordinates if we need it
# def get_mouse_click_coor(x,y,):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

guessing = True
score = 0
correct_guesses = []
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

while guessing:
    answer_state = screen.textinput(title=f"{score}/50 States Guessed", prompt="What is a state name?").title()
    
    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in correct_guesses:
                missing_states.append(state)
        missing_data = pd.DataFrame(missing_states)
        missing_data.to_csv("states_to_learn.csv")
        break

    if states_info['state'].str.contains(answer_state).any() and answer_state not in correct_guesses:
       info = states_info.loc[states_info["state"] == answer_state].values.flatten().tolist()
       x, y = info[1], info[2]
       writer.goto(x, y) 
       writer.write(info[0])
       score += 1
       correct_guesses.append(info[0])

    if score == 50:
        guessing = False

# screen.exitonclick()