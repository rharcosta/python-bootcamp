student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = student_scores

for student, score in student_grades.items():
    if 91 < score < 100:
        student_grades[student] = "Outstanding"
    elif 81 < score < 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 < score < 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
