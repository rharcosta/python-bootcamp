from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import os

load_dotenv()

username = os.environ["LINKEDIN_USERNAME"]
password = os.environ["LINKEDIN_PASSWORD"]
phone_number = os.environ["LINKEDIN_PHONE"]


def abort_application():
    # click close button
    close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # click discard button
    discard_button = driver.find_elements(By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[0]
    discard_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3959763086&f_AL=true&geoId=104102503&keywords"
           "=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")

driver.maximize_window()

# reject cookies button
time.sleep(2)
reject_button = driver.find_element(By.CSS_SELECTOR, value="button[action-type='DENY']")
reject_button.click()

# enter button
time.sleep(2)
sign_in = driver.find_element(By.CLASS_NAME, value="btn-secondary-emphasis")
sign_in.click()

# username and password
time.sleep(2)
username_field = driver.find_element(By.ID, value="username")
username_field.send_keys(username)

password_field = driver.find_element(By.ID, value="password")
password_field.send_keys(password, Keys.ENTER)

# solve CAPTCHA manually
# input("Press enter when you have solved the Captcha.")

# get the list of applications
time.sleep(5)
all_listing = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")

# apply for jobs
for listing in all_listing:
    listing.click()
    time.sleep(2)
    try:
        # click to apply
        apply_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # insert phone number
        time.sleep(2)
        phone = driver.find_element(By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == " ":
            phone.send_keys(phone_number)

        # check the submit button
        submit_button = driver.find_element(By.CSS_SELECTOR, value="footer button")
        submit_button.click()
        if submit_button.get_attribute("ariaLabel") == "Avançar para próxima etapa":
            print("Complex application skipped.")
            abort_application()
            continue
        else:
            print("Submitting job application!")
            # submit_button.click()

        time.sleep(2)
        abort_application()

    except NoSuchElementException:
        print("No application button. Skipped.")
        abort_application()
        continue

time.sleep(5)
driver.quit()
