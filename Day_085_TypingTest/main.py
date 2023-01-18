from tkinter import *
from phraselist import phrases
import random
import time

window = Tk()
window.minsize(width=800, height=600)

phrase = random.choice(phrases)

def key(event):
     text= event.char
     text+= event.char
     print(text)

frame = Frame(window, width=100, height=100)
frame.bind("<Key>", key)
frame.pack()

starting_time = 0

def start_time(event):
    global starting_time
    
    if not starting_time:
        starting_time = time.time()
    return starting_time

def check_phrase(event):
    end_time = time.time()
    correct_phrase = phrase
    entry_phrase = type_box.get()
    total = len(correct_phrase)
    correct = 0
    for x, y in zip(correct_phrase, entry_phrase):
        if x == y:
            correct += 1
    ratio = correct/total
    ratio_perc = round(ratio*100,2)
    speed = round(end_time-starting_time,2)
    speed_to_char = (len(phrase)/speed)*60
    wpm = round(speed_to_char/4.7)
    speed_label['text'] = f"You had an accuracy of: {ratio_perc}% and a speed of {speed}s with a wpm of {wpm}"
    # print(ratio)
    # print(end_time-starting_time)
    return ratio
        
# Checking function works as intended
# ratio = check_phrase("We are champions", "We are chumpions")
# print(ratio)

phrase_label = Label(window, text=phrase)
phrase_label.pack()

window.bind('<Key>', start_time)

type_box = Entry(window)
type_box.pack()
ratio = window.bind('<Return>', check_phrase)

speed_label = Label(window, text=f"")
# window.bind('<Return>', update_speed)
speed_label.pack()

window.mainloop()