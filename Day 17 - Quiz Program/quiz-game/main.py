from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for each in question_data:
    question_text = each["text"]
    question_answer = each["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

if not quiz.still_has_question():
    print(f"\n* You've completed the quiz. Your final score was {quiz.score} out of {quiz.question_number}.")
