from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import smtplib
import os

load_dotenv()
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
              "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "priority": "u=0",
    "upgrade-insecure-requests": "1",
}
url = ("https://www.amazon.it/Apple-iPhone-Pro-Max-256/dp/B0CHX4FBSK/ref=sr_1_3?dib=eyJ2IjoiMSJ9.XNRlm_vLosJqticRgar"
       "ONC8fQXpP2QPSUy6Ksk5O6ATBE9iINit_jJslVuk3Yr_KuCAGaQMQ-rOalMaFwCo6LFU3KlXAjgLo8fIBtbh4E-oM8C4IVUgcB_o5S-aCYgapl"
       "tW1mRwMHtzi-owFckmweKiA6raXnNyKdkFpnWYCIdKLsYWfpD27WhoQERnt-B8ctSSTn7i2vm2DoO24ZlokWDPVcSgkXFVtR6riJbZ4xJpa8sf"
       "bEwqEu4PqErsXKA1wwP_h8C47DPCppkbv4nSxQ21z3CeCNNHUQlXXxECV9Sw.H0dLtuQFdQ0vwWYkpYUpI2bwq4nXTd4nR5ha2V0AJTo&dib_"
       "tag=se&keywords=iphone+15+pro+max&qid=1721584305&sr=8-3")

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

price_string = soup.find(name="span", class_="a-price-whole").get_text().split(",")[0]
price = float(price_string)
title = soup.find(name="span", id="productTitle").get_text().strip()
message = f"{title} is on sale for {price} euros!"

# ------------------ SEND AN EMAIL ------------------

buy_price = 1200

email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]
address = os.environ["SMTP_ADDRESS"]

if price < buy_price:
    with smtplib.SMTP(address) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email,
                            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8"))
        print("Successful!")
