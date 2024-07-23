from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

driver.maximize_window()

# get cookie
cookie = driver.find_element(By.ID, value="cookie")

# get upgrade item
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
# storing into an array all the id items
item = [one.get_attribute("id") for one in items]

timeout = time.time() + 5  # five seconds
five_min = time.time() + 60 * 5  # five minutes

while True:
    cookie.click()

    # every five seconds
    if time.time() > timeout:
        # get all prices
        prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # convert <b> text into an integer price
        for price in prices:
            element = price.text
            if element != "":
                cost = int(element.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # dictionary of items and prices
        upgrades = {}
        for n in range(len(item_prices)):
            upgrades[item_prices[n]] = item[n]

        # get the current cookie count
        money = driver.find_element(By.ID, value="money").text
        if "," in money:
            money = money.replace(",", "")
        count = int(money)

        # find items that we can currently afford
        affordable_upgrades = {}
        for cost, ident in upgrades.items():
            if count > cost:
                affordable_upgrades[cost] = ident

        # purchase the most expensive item
        highest_price = max(affordable_upgrades)
        to_purchase = affordable_upgrades[highest_price]

        driver.find_element(By.ID, value=to_purchase).click()

        # add another 5 seconds until the next check
        timeout = time.time() + 5

        # after five minutes stop the bot and check the cookies per second count
        if time.time() > five_min:
            cookie_sec = driver.find_element(By.ID, value="cps").text
            print(cookie_sec)
            break
