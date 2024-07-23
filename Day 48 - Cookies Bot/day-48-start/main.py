from selenium import webdriver
from selenium.webdriver.common.by import By

# keep the browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# open the chrome
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.it/CeraVe-Lozione-Idratante-Corpo-Detergente/dp/B096XZZ9YQ/?_encoding=UTF8&pd_rd_w=fuQFm&content-id=amzn1.sym.17588632-908c-4d26-92c5-2e25c2c0269c%3Aamzn1.symc.cdb151ed-d8fe-485d-b383-800c8b0e3fd3&pf_rd_p=17588632-908c-4d26-92c5-2e25c2c0269c&pf_rd_r=1060SP39H20Z17GYFC6D&pd_rd_wg=aZzou&pd_rd_r=be19d8d8-af89-4b6b-82e7-442dd9eff4e3&ref_=pd_hp_d_atf_ci_mcx_mr_hp_atf_m&th=1")

price = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
print(f"The price is {price}.{cents}")

# search by NAME
# search_bar = driver.find_element(By.NAME, value="q").tag_name
# or .get_attribute("placeholder")

# search by ID
# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# search inside an element
# driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# driver.find_element(By.XPATH, value="path - copy and paste")

# close a single tab: driver.close()
# close the entire browser driver.quit()
