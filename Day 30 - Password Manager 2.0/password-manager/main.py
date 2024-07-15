from tkinter import *
from tkinter import messagebox  # this is not a class, that's why we need to import
from random import choice, randint, shuffle
import pyperclip  # will copy my password automatically
import json


# ---------------------------- PASSWORD GENERATOR -------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    x = "".join(password_list)
    password_entry.insert(0, x)
    pyperclip.copy(x)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Blank Fields", message="Please make sure you haven't left any fields empty.")
    else:
        confirmation = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                                     f"Email: {email}\nPassword: {password}\n"
                                                                     f"Do you confirm saving them?")

        if confirmation:
            try:
                with open("data.json", "r") as data_file:
                    # reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)  # from 0 to the end
                password_entry.delete(0, END)
                website_entry.focus()
                messagebox.showinfo(title="Completed", message="Saved Data")


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------------ #
# window
window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

# canvas
image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.insert(0, "user@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=2)

# buttons
btn_search = Button(text="Search", width=15, command=find_password)
btn_search.grid(column=3, row=2)
btn_password = Button(text="Generate Password", width=15, command=generate_password)
btn_password.grid(column=3, row=3)
btn_add = Button(text="Add", width=30, command=save)
btn_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
