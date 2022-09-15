from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(3, 6))]
    password_numbers = [choice(numbers) for _ in range(randint(3, 6))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, f'{password}')
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    email = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Missing Values", message="Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details enter:\n Website: {website} \n Email: {email}"
                                                    f"\nPassword:{password} \n Is it okay to save?")
        
        if is_ok:
            with open('password.txt', 'a') as pw_text:
                pw_text.write(f'{email} | {website} | {password}\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
    

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

password_gen = Button(text="Generate Password", command=password_generator)
password_gen.grid(column=2, row=3)


# Add Button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()