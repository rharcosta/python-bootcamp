from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from dotenv import load_dotenv
from time import sleep
import os

load_dotenv()
account = os.environ["SIMILAR_ACCOUNT"]
username = os.environ["INSTAGRAM_USERNAME"]
password = os.environ["INSTAGRAM_PASSWORD"]


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()

    def login(self):
        # refuse cookies
        sleep(2)
        self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Recusar cookies opcionais')]").click()
        # username
        sleep(2)
        self.driver.find_element(By.NAME, value="username").send_keys(username)
        # password
        sleep(2)
        self.driver.find_element(By.NAME, value="password").send_keys(password, Keys.ENTER)

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{account}")
        # following
        sleep(2)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, value="seguindo").click()

        # scrolling the bar
        sleep(5)
        modal = self.driver.find_element(By.XPATH, value="/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div"
                                                         "/div/div/div[2]/div/div/div[4]")

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.XPATH, value="//div[contains(text(), 'Seguir')]")

        for button in all_buttons:
            try:
                button.click()
                sleep(2)
            # if you are already following someone
            except ElementClickInterceptedException:
                # cancel button
                self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Cancelar')]").click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
