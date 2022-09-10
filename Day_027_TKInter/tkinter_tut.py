from tkinter import *

window = Tk()
window.minsize(width=600, height= 400)


# TK Labels
my_label = Label(text = "This is a label", font=("Arial", 24, "bold"))
my_label.pack()
my_label['text'] = "New Text" # One option for changing text 

# TK Buttons

def button_click():
    my_label.config(text="I got clicked") # Other option for changing text in label
    print("I got clicked")

button = Button(text="Click Me", command=button_click)
button.pack()

# TK Entry

input = Entry(width = 20, string="New Label Here")
input.pack()

def text_changer():
    my_label.config(text=input.get())

button_two = Button(text="Change Text Here", command=text_changer)
button_two.pack()




window.mainloop()