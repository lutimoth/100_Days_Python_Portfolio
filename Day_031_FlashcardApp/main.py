import pandas as pd
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

CARD_FRONT = './images/card_front.png'
CARD_BACK = './images/card_back.png'
RIGHT = './images/right.png'
WRONG = './images/wrong.png'

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg= BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file=CARD_FRONT)
canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)


right_image = PhotoImage(image=RIGHT)
right_button = Button(image=right_image, highlightthickness=0)
# wrong_image = PhotoImage(image=WRONG)


window.mainloop()
