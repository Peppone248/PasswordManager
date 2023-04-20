import random
import string
from tkinter import *
from tkinter import messagebox

FONT_NAME = "Montserrat"
FONT_SIZE = 12

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
psw_length = [8, 9, 10, 11, 12]
characters = string.ascii_letters + string.digits + string.punctuation


def generate_psw():
    input_psw.delete(0, END)
    psw = ''.join(random.choice(characters) for i in range(random.choice(psw_length)))
    input_psw.insert(0, psw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(input_psw.get()) == 0 or len(input_site.get()) == 0:
        messagebox.showinfo(title="WARNING", message="Fill the fields to continue!")
    else:
        is_ok = messagebox.askokcancel(title=input_site.get(),
                                       message=f"There are the credentials entered: \nEmail: {input_mail.get()}"
                                               f"\nPassword: {input_psw.get()} \n Are you sure?")

        if is_ok:
            with open("data.txt", 'a+') as f:
                f.write(f"{input_site.get()} , {input_mail.get()} , {input_psw.get()}\n")
                input_site.delete(0, END)
                input_mail.delete(0, END)
                input_psw.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("CryptPass - The Password Manager")
window.config(padx=80, pady=80)
canvas = Canvas(width=200, height=200)
padlock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock)
canvas.grid(column=1, row=0)

# LABELS
name_site_lbl = Label(text="Website:")
name_site_lbl.grid(column=0, row=1)

mail_lbl = Label(text="Email/Username:")
mail_lbl.grid(column=0, row=2)

psw_lbl = Label(text="Password:")
psw_lbl.grid(column=0, row=3)

# ENTRIES
input_site = Entry(width=35)
input_site.grid(column=1, row=1, columnspan=2)
input_site.focus()

input_mail = Entry(width=35)
input_mail.grid(column=1, row=2, columnspan=2)
input_mail.insert(0, "pippo@pluto.com")

input_psw = Entry(width=35)
input_psw.grid(column=1, row=3, columnspan=2)

# BUTTONS
add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=6, columnspan=2)

generate_psw_btn = Button(text="Generate Password", command=generate_psw)
generate_psw_btn.grid(column=1, row=4)

window.mainloop()
