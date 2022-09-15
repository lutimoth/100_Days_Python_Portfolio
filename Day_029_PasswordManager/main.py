from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=25)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


# Website Info
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=36)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)


# Email Info
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "lutimoth@usc.edu")

# Password Info
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

password_gen = Button(text="Generate Password")
password_gen.grid(column=2, row=3)


# Add Button
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()