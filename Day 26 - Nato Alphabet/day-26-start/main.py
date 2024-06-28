from random import randint
import pandas

# list comprehension
numbers = [1, 2, 3]
new_numbers = [item+1 for item in numbers]
# print(new_numbers)

name = "Rubia"
new_name = [letter for letter in name]
# print(new_name)

range_list = [double * 2 for double in range(1, 5)]
# print(range_list)

# conditional list comprehension
names = ["Alex", "Beth", "David", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
# print(short_names)

upper_names = [name.upper() for name in names if len(name) > 4]
# print(upper_names)

# dictionary comprehension
students_name = ["Alex", "Beth", "David", "Eleanor", "Freddie"]
students_score = {student: randint(1, 100) for student in students_name}
# print(students_score)

# new_key: new_value
passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
# print(passed_students)

# pandas + dictionaries
students_dict = {
    "students": ["Rubia", "Marco", "Angela"],
    "scores": [100, 50, 75]
}
students_data = pandas.DataFrame(students_dict)
print(students_data)

for (index, row) in students_data.iterrows():
    print(row)
