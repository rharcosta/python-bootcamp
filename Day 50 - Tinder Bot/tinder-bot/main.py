from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv()
email = os.environ["TINDER_EMAIL"]
password = os.environ["TINDER_PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.tinder.com")
driver.maximize_window()

# deny cookies
time.sleep(2)
cookies = driver.find_element(By.XPATH, value="//*[@id='q1503199108']/div/div[2]/div/div/div[1]/div[2]/button")
cookies.click()

# login button
time.sleep(2)
login_button = driver.find_element(By.LINK_TEXT, value="Entrar")
login_button.click()

# facebook login
time.sleep(5)
fb_login = driver.find_element(By.XPATH, value='//*[@id="q-225181968"]/div/div/div/div[1]/div/div/div[2]/div[2]'
                                               '/span/div[2]/button')
fb_login.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email_field = driver.find_element(By.XPATH, value='//*[@id="email"]')
email_field.send_keys(email)

password_field = driver.find_element(By.XPATH, value='//*[@id="pass"]')
password_field.send_keys(password, Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

# allow location button
time.sleep(5)
allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

# not interested into notifications
notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

# accept cookies
cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

# tinder free tier only allows 100 "Likes" per day
for n in range(100):
    # add a one-second delay between likes
    time.sleep(1)

    try:
        like_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div'
                                                          '/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    # catches the cases where there is a "Matched" pop-up in front of the "Like" button
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        # catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
