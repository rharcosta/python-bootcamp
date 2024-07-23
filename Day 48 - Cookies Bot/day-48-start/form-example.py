from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Rubia")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Costa")

email_address = driver.find_element(By.NAME, value="email")
email_address.send_keys("rubia@gmail.com")

bottom = driver.find_element(By.CSS_SELECTOR, value="form button")
bottom.send_keys(Keys.ENTER)
