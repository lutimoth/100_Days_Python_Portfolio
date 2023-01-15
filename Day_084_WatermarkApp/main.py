from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.geometry("800x600")
window.title("Image Watermarker")

FONT = ('times', 18, 'bold')

title = Label(window, text="Image Watermark Generator", width=30, font=FONT)
title.grid(row=1,column=1)

upload_button = Button(window, text="Upload Image")
upload_button.grid(row=2,column=1)

window.mainloop()