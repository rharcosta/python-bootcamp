import pandas
from random import choice
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(background, image=canvas_front_img)
    timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(background, image=canvas_back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------- File ------------------------ #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------- Screen ---------------------- #
# window
window = Tk()
window.title("Flash Cards Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_front_img = PhotoImage(file="./images/card_front.png")
canvas_back_img = PhotoImage(file="./images/card_back.png")
background = canvas.create_image(400, 263, image=canvas_front_img)
canvas.grid(column=0, row=0, columnspan=2)

# labels
title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

# buttons
wrong_image = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=wrong_image, highlightthickness=0, command=next_card)
btn_wrong.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
btn_right = Button(image=right_image, highlightthickness=0, command=is_known)
btn_right.grid(column=1, row=1)

next_card()
window.mainloop()
