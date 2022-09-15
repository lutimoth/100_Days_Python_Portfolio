from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    countdown(25*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = count // 60
    count_sec = count % 60

    if count_sec <= 9:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, countdown, count-1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

timer_text = Label(text="Timer", fg= GREEN, font=(FONT_NAME, 42, "bold"), bg=YELLOW)
timer_text.grid(column=1, row=0)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="./tomato.png")
canvas.create_image(103, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 12), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME,12), highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmark = Label(text="✓", fg=GREEN, font=(FONT_NAME, 15), bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()