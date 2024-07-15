import pandas as pd
import smtplib
from random import randint
from datetime import datetime

file = pd.read_csv("birthdays.csv")

today = (datetime.now().day, datetime.now().month)
dictionary = {(data["day"], data["month"]): data for (index, data) in file.iterrows()}
# print(dictionary)

if today in dictionary:
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
    with open(file_path) as letter:
        read_letter = letter.read()
        birthday_person = dictionary[today]
        new_letter = read_letter.replace("[NAME]", birthday_person["name"])
        print(new_letter)

        my_email = "t1838285@gmail.com"
        password = "kkhosqztttzpmlmx"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_person["email"],
                                msg=f"Subject: Happy Birthday!\n\n{new_letter}"
                                )
