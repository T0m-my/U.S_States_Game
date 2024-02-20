import turtle

screen = turtle.Screen()
screen.title('U.S. States Game')

img = 'blank_states_img.gif'
turtle.addshape(img)
turtle.shape(img)

answer = screen.textinput(title='Guess State Name', prompt='What\'s another state\'s name?')
print(answer)

# screen.exitonclick()
turtle.mainloop()
