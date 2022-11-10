from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import time

load_dotenv()

URL = os.getenv('URL')
USER = os.getenv('USER')
PW = os.getenv('PASSWORD')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chromedrive_directory = os.getenv('CHROME_PATH')
driver = webdriver.Chrome(service=Service(chromedrive_directory))

driver.get(URL)

time.sleep(2)

signin_button = driver.find_element(By.CSS_SELECTOR, "a.nav__button-secondary")
signin_button.click()

time.sleep(2)

user_fill = driver.find_element(By.ID,'username')
user_fill.send_keys(USER)

pw_fill = driver.find_element(By.ID,'password')
pw_fill.send_keys(PW)

login_button = driver.find_element(By.TAG_NAME, 'button')
login_button.click()

time.sleep(2)


def job_hunt():
    jobs = driver.find_elements(By.CLASS_NAME, 'job-card-container')

    for job in jobs:
        job.click()
        time.sleep(2)
        try:
            easy_apply = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
            easy_apply.click()
            time.sleep(2)
            
            easy_text = driver.find_element(By.XPATH, "//span[text()='Submit application']")
            #print(easy_text)

            easy_text.text == 'Submit application'
            #print(f"The text is {easy_text}")
            submit_button = driver.find_element(By.XPATH, "//*[@aria-label='Submit application']") 
            submit_button.click()
            time.sleep(2)
            done_button = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
            done_button.click()
            time.sleep(2)
            # else:
            #     cancel_button = driver.find_element(By.XPATH, "//*[@aria-label='Dismiss']")
            #     cancel_button.click()
            #     time.sleep(2)
            #     discard_button = driver.find_element(By.XPATH, "//*[@data-control-name='discard_application_confirm_btn']")
            #     discard_button.click()
            #     time.sleep(2)
        except NoSuchElementException:
            cancel_button = driver.find_element(By.XPATH, "//*[@aria-label='Dismiss']")
            cancel_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.XPATH, "//*[@data-control-name='discard_application_confirm_btn']")
            discard_button.click()
            time.sleep(2)

page_numbers = driver.find_elements(By.CLASS_NAME, 'artdeco-pagination__indicator')
last_number = int(page_numbers[-1].text)

for i in range(1, last_number):
    job_hunt()
    time.sleep(2)
    # on_screen_numbers = driver.find_element(By.CLASS_NAME, 'artdeco-pagination__indicator')
    next_page = driver.find_element(By.XPATH, f'//*[@aria-label="Page {i+1}"]')
    next_page.click()
    time.sleep(2)