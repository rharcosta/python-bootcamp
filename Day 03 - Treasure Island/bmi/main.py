weight = 65
height = 1.63

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif 18.5 < bmi < 25:
    print("Normal weight")
else:
    print("Overweight")
