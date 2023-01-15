from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

window = Tk()
window.geometry("800x600")
window.title("Image Watermarker")

FONT = ('times', 18, 'bold')

title = Label(window, text="Image Watermark Generator", width=30, font=FONT)
title.grid(row=1,column=1)

upload_button = Button(window, text="Upload Image", command=lambda:upload_file())
upload_button.grid(row=2,column=1)

def upload_file():
    global img
    file_types = [('Jpg files','*.jpg')]
    file_name = filedialog.askopenfilename(filetypes=file_types)
    img = ImageTk.PhotoImage(file=file_name)
    b2 = Button(window, image=img) # using Button 
    b2.grid(row=3,column=1)

window.mainloop()