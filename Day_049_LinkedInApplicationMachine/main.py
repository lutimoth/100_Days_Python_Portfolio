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

chromedrive_directory = "C:/Users/lutimoth/Documents/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(service=Service(chromedrive_directory))

driver.get(URL)

time.sleep(5)

signin_button = driver.find_element(By.CSS_SELECTOR, "a.nav__button-secondary")
signin_button.click()

time.sleep(5)

user_fill = driver.find_element(By.ID,'username')
user_fill.send_keys(USER)

pw_fill = driver.find_element(By.ID,'password')
pw_fill.send_keys(PW)

login_button = driver.find_element(By.TAG_NAME, 'button')
login_button.click()

time.sleep(5)

jobs = driver.find_elements(By.CLASS_NAME, 'job-card-container')

for job in jobs:
    job.click()
    time.sleep(3)
    easy_apply = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
    easy_apply.click()
    time.sleep(5)
    easy_text = driver.find_element(By.CLASS_NAME, 'artdeco-button__text')
    
    if easy_text.text == 'Submit Application':
        submit_button = driver.find_element(By.CLASS_NAME, 'artdeco-button')
        submit_button.click()
        time.sleep(5)
        submit_button.click()
        time.sleep(5)
    else:
        cancel_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismissal')