from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont

window = Tk()
window.minsize(width=800, height=600)
window.title("Image Watermarker")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

FONT = ('times', 18, 'bold')

title_label = Label(window, text="Image Watermark Generator", font=FONT)
title_label.grid(column=0, row=1, columnspan=2)

upload_button = Button(window, text="Upload Image", command=lambda:upload_file())
upload_button.grid(column=0,row=2)

watermark_button = Button(window, text="Create Watermark", command=lambda:create_watermark(canvas))
watermark_button.grid(column=1, row=2)

def upload_file():
    global img
    global canvas
    file_types = [('Jpg files','*.jpg')]
    file_name = filedialog.askopenfilename(filetypes=file_types)
    img = ImageTk.PhotoImage(file=file_name)
    canvas = Canvas(window, width=img.width(), height=img.height())
    canvas.create_image(2, 2, image=img, anchor='nw')
    canvas.grid(column=0, row=3,columnspan=2)

def create_watermark(canvas):
    width, height = img.width(), img.height()
    text = "Timothy Lu"

    margin = 50
    x = width - margin 
    y = height - 10
    
    canvas_text = canvas.create_text(x, y)
    canvas.itemconfig(canvas_text, text=text, font=('courier',12), fill="white")

window.mainloop()