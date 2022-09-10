from cProfile import label
from tkinter import *
from tkinter.tix import InputOnly

window = Tk()
window.minsize(width=300, height= 50)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

km_convert = Label(text="0")
km_convert.grid(column=1,row=1)

miles_input = Entry(width=20)
miles_input.grid(column=1,row=0)

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609,2)
    km_convert.config(text=str(km))

convert_button = Button(text="Calculate", command=miles_to_km)
convert_button.grid(column=1,row=2)

window.mainloop()