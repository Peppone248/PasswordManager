import random
import string
import json
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
    website = input_site.get()
    email = input_mail.get()
    psw = input_psw.get()
    new_data = {
        website: {
            "email": email,
            "password": psw,
        }
    }
    if len(input_psw.get()) == 0 or len(input_site.get()) == 0:
        messagebox.showinfo(title="WARNING", message="Fill the fields to continue!")
    else:
        try:
            with open("data.json", 'r') as f:
                # Read old data
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", 'w') as f:
                json.dump(new_data, f)
        else:
            # Update old data with new
            data.update(new_data)
            with open("data.json", 'w') as f:
                # Write new update date
                json.dump(data, f)
        finally:
            input_site.delete(0, END)
            input_mail.delete(0, END)
            input_psw.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    site = input_site.get()
    with open("data.json") as file:
        data = json.load(file)
        if site in data:
            email = data[site]["email"]
            psw = data[site]["password"]
            messagebox.showinfo(title="Information", message=f"Email: {email}\nPassword: {psw}")


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
add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(column=1, row=6, columnspan=2)

generate_psw_btn = Button(text="Generate Password", width=35, command=generate_psw)
generate_psw_btn.grid(column=1, row=4, columnspan=2)

search_btn = Button(text="Search", width=15, command=find_password)
search_btn.grid(column=3, row=1)

window.mainloop()
