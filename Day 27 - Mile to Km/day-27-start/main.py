from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(400, 400)
window.config(padx=20, pady=20)  # give space before starting the action on the screen

label = Label(text="I am a label", font=("Arial", 24, "bold"))
label.pack()  # to show the label in the screen
# label.pack(expand=True) # label in central
# label.pack(side="left") # label in left

# changing the label
label["text"] = "New Text =D"
# or
label.config(text="New Text")


# button
def button_clicked():
    # print("I got clicked")
    # label.config(text="Button Got Clicked")
    label.config(text=user_input.get())  # user input will be written in the label


button = Button(text="Click me", command=button_clicked)
button.pack()

# entry
user_input = Entry(width=20)
user_input.pack()

# text box
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
text.get("1.0", END)  # starting in the first line in character 0
text.pack()

# spin box
spinbox = Spinbox(from_=0, to=10, width=5)
spinbox.pack()

# scale
scale = Scale(from_=0, to=100)
scale.pack()

# checkbutton
state = IntVar()
check = Checkbutton(text="Is on?", variable=state)
check.pack()

# radiobutton
radio_state = IntVar()
radio1 = Radiobutton(text="Option 1", value=1, variable=radio_state)
radio2 = Radiobutton(text="Option 2", value=2, variable=radio_state)
radio3 = Radiobutton(text="Option 3", value=3, variable=radio_state)
radio1.pack()
radio2.pack()
radio3.pack()


# listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# .pack()
# .place(0, 0)
# .grid(column=1, row=1)
# they can't be used combined, you need to choose one

window.mainloop()  # to show the window
