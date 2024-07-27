from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, "html.parser")

list_links = [links.get("href") for links in soup.select(".StyledPropertyCardDataWrapper a")]
list_prices = [prices.getText().strip("\n+/mo+ 1bd") for prices in soup.select("div div .PropertyCardWrapper")]
list_addresses = [addresses.getText().strip("\n ") for addresses in soup.select("div div a address")]

print(list_links)
print(list_prices)
print(list_addresses)

# popup the data to google forms
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://forms.gle/1Rv8v7iEUgJ9KBAUA")
driver.maximize_window()

for i in range(len(list_links)):
    sleep(2)

    # address
    field_address = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]"
                                                        "/div/div[1]/div/div[1]/input")
    field_address.send_keys(list_addresses[i])

    # price
    field_price = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]"
                                                      "/div/div[1]/div/div[1]/input")
    field_price.send_keys(list_prices[i])

    # link
    field_link = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]"
                                                     "/div/div[1]/div/div[1]/input")
    field_link.send_keys(list_links[i])

    # send button
    driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div").click()

    # send another answer
    driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()
