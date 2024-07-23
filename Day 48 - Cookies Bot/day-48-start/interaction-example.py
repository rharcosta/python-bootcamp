from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article.click()

# clicking in a link
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# searching for something
driver.maximize_window()
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

# driver.close()
