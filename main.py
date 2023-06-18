from tkinter import *
from functools import partial
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for _ in range(randint(8, 18))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email} "
                                                          f"\nPassword:{password} \nIs it ok to save?")

    if is_ok:
        with open("readme.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            entry_website.delete(0, END)
            entry_password.delete(0, END)
            entry_email.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=1)


def label(text, column, row):
    my_label = Label(text=f"{text}", font=("Arial", 10, "bold"))
    my_label.grid(column=column, row=row)


label("Website:", 0, 2)
entry_website = Entry(window, width=35)
entry_website.grid(column=1, row=2, columnspan=2)
entry_website.focus()

label("Email/Username:", 0, 3)
entry_email = Entry(window, width=35)
entry_email.grid(column=1, row=3, columnspan=2)

label("Password:", 0, 4)
entry_password = Entry(window, width=27)
entry_password.grid(column=1, row=4)



# Buttons
button_generate = Button(text="Generate password", command=generate_password)
button_generate.grid(column=2, row=4)

button = Button(text="Add", width=30, command=add)
button.grid(column=1, row=5, columnspan=2)

mainloop()
