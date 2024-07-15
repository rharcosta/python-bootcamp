from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=FONT)
        self.score.grid(column=1, row=0)

        # canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, text="Quiz Game", font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # buttons
        right_image = PhotoImage(file="images/true.png")
        self.btn_right = Button(image=right_image, highlightthickness=0, bg=THEME_COLOR, command=self.true_pressed)
        self.btn_right.grid(column=0, row=2)
        wrong_image = PhotoImage(file="images/false.png")
        self.btn_wrong = Button(image=wrong_image, highlightthickness=0, bg=THEME_COLOR, command=self.false_pressed)
        self.btn_wrong.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.btn_right.config(state="disabled")
            self.btn_wrong.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
