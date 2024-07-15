from tkinter import *

window = Tk()
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)
window.title("Mile to KM Conversor")
design = ("Arial", 10)


def conversor():
    mile = entry.get()
    km = float(mile) * 1.609
    label3.config(text=round(km, 2))


entry = Entry(width=20, justify="center")
entry.focus()
entry.grid(column=2, row=1)

label1 = Label(text="Miles", font=design)
label1.grid(column=3, row=1)

label2 = Label(text="is equal to", font=design)
label2.grid(column=1, row=2)

label3 = Label(text="0", font=design)
label3.grid(column=2, row=2)

label4 = Label(text="KM", font=design)
label4.grid(column=3, row=2)

button = Button(text="Calculate", command=conversor)
button.grid(column=2, row=3)

window.mainloop()
