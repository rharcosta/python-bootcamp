from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from time import sleep
import os

load_dotenv()
PROMISED_DOWN = 150
PROMISED_UP = 10
EMAIL = os.environ["TWITTER_EMAIL"]
PASSWORD = os.environ["TWITTER_PASSWORD"]


class InternetSpeedTwitterBot:

    def __init__(self):
        self.down = 0
        self.up = 0

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()

        # reject cookies
        self.driver.find_element(By.ID, value="onetrust-reject-all-handler").click()

        # go button
        self.driver.find_element(By.XPATH, value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]"
                                                 "/div[1]/a").click()

        sleep(60)
        self.down = self.driver.find_element(By.XPATH, value="//*[@id='container']/div/div[3]/div/div/div"
                                                             "/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]"
                                                             "/div[1]/div[1]/div/div[2]/span").text
        self.up = self.driver.find_element(By.XPATH, value="//*[@id='container']/div/div[3]/div/div/div"
                                                           "/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]"
                                                           "/div[1]/div[2]/div/div[2]/span").text
        print(f"Download = {self.down}\nUpload = {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://x.com/login")
        self.driver.maximize_window()

        # email
        sleep(4)
        self.driver.find_element(By.NAME, value="text").send_keys(EMAIL, Keys.ENTER)

        # password
        sleep(4)
        self.driver.find_element(By.NAME, value="password").send_keys(PASSWORD, Keys.ENTER)

        # text
        message = (f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when "
                   f"I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        sleep(4)
        self.driver.find_element(By.XPATH, value="//*[@id='react-root']/div/div/div[2]/main/div/div/div/div"
                                                 "/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]"
                                                 "/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div"
                                                 "/div/div/div/div[2]/div/div/div/div"
                                 ).send_keys(message)

        # post
        sleep(4)
        self.driver.find_element(By.XPATH, value="//*[@id='react-root']/div/div/div[2]/main/div/div/div/div"
                                                 "/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]"
                                                 "/div[2]/div/div/div/button").click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
