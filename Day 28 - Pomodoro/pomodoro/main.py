from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#36BA98"
YELLOW = "#f7f5dd"
FONT_NAME = ("Courier", 26, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetition = 0
my_timer = ""


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    check_mark.config(text="")
    global repetition
    repetition = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
# 25 min work -> 5 min break
# -> 25 min work -> 5 min break
# -> 25 min work -> 5 min break
# -> 25 min work -> 20 min break

def start_timer():
    global repetition
    repetition += 1

    work = WORK_MIN * 60  # changing to minutes
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if repetition == 9:
        reset()

    # if it's the 8th repetition -> long break
    elif repetition % 8 == 0:
        count_down(long_break)
        label_timer.config(text="Break", fg=PINK)

    # if it's the 2nd/4th/6th repetition -> short break
    elif repetition % 2 == 0:
        count_down(short_break)
        label_timer.config(text="Break", fg=RED)

    # if it's the 1st/3rd/5th/7th repetition ->  work
    else:
        count_down(work)
        label_timer.config(text="Work Time", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global my_timer
    count_min = floor(count / 60)  # return the integer number
    count_sec = count % 60
    # dynamic typing - convert a type of variable
    # if count_sec < 10:
    #     count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        my_timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        number_work = floor(repetition / 2)
        for _ in range(number_work):
            marks += "✅"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=30, bg=YELLOW)

# setting my screen to upload the image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# 'high light thick ness' - remove the background of the image
tomato = PhotoImage(file="tomato.png")

# canvas image and timer
canvas.create_image(100, 112, image=tomato)  # values are half of the canvas values
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=FONT_NAME)
canvas.grid(column=2, row=2)

# label timer
label_timer = Label(text="Timer", bg=YELLOW, font=FONT_NAME, fg=GREEN)
label_timer.grid(column=2, row=1)

# buttons
button_start = Button(text="Start", command=start_timer)
button_start.grid(column=1, row=3)
button_reset = Button(text="Reset", command=reset)
button_reset.grid(column=3, row=3)

# checkmark
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))
check_mark.grid(column=2, row=3)

window.mainloop()
