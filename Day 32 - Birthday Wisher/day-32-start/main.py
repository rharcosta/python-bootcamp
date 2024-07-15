import random
import datetime as dt
import smtplib  # SMTP (Simple Mail Transfer Protocol)

my_email = "t1838285@gmail.com"  # testing email created
password = "kkhosqztttzpmlmx"  # generate an app password in mail application

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:
    with open("quotes.txt", encoding="UTF-8") as file:
        lines = file.readlines()
        random_quote = random.choice(lines)
    print(random_quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # smtp.live.com / smtp.mail.yahoo.com
        connection.starttls()  # starting the connection secure
        connection.login(user=my_email, password=password)
        message = f"Subject:Wednesday Motivation\n\n{random_quote}"
        connection.sendmail(from_addr=my_email,
                            to_addrs="appbrewerytesting@yahoo.com",
                            # the message is encoded in UTF-8 to ensure that special characters are supported
                            msg=message.encode("utf-8")
                            )
