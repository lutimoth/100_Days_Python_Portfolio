from tkinter import *
from phraselist import phrases
import random

window = Tk()
window.minsize(width=800, height=600)

phrase = random.choice(phrases)

# def key(event):
#      text= event.char
#      text+= event.char
#      print(text)

# frame = Frame(window, width=100, height=100)
# frame.bind("<Key>", key)
# frame.pack()

phrase_label = Label(window, text=phrase)
phrase_label.pack()

type_box = Entry(window)
type_box.pack()

window.mainloop()