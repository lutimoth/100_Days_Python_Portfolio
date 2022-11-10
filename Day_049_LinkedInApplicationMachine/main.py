from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import os
from dotenv import load_dotenv
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

time.sleep(10)

def job_hunt():
    jobs = driver.find_elements(By.CLASS_NAME, 'job-card-container')
    #job_list = driver.find_element(By.CLASS_NAME, 'jobs-search-results-list')
    for job in jobs:
        job.click()
        time.sleep(2)
        try:
            easy_apply = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
            easy_apply.click()
            time.sleep(1)
            
            # easy_text = driver.find_element(By.XPATH, "//span[text()='Submit application']")
            # easy_text.text == 'Submit application'
            submit_button = driver.find_element(By.XPATH, "//*[@aria-label='Submit application']") 
            submit_button.click()
            time.sleep(3)
            done_button = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
            done_button.click()
            time.sleep(2)
            # driver.refresh()
            # time.sleep(3)
            # jobs = driver.find_elements(By.CLASS_NAME, 'job-card-container')
            # time.sleep(1)
        except NoSuchElementException:
            try:
                cancel_button = driver.find_element(By.XPATH, "//*[@aria-label='Dismiss']")
                cancel_button.click()
                time.sleep(2)
                discard_button = driver.find_element(By.XPATH, "//*[@data-control-name='discard_application_confirm_btn']")
                discard_button.click()
                time.sleep(2)
            except ElementNotInteractableException:
                continue
            except StaleElementReferenceException:
                driver.refresh()
                time.sleep(3)
                jobs = driver.find_elements(By.CLASS_NAME, 'job-card-container')
                time.sleep(1)
        ActionChains(driver).move_to_element(job).pause(1).scroll_by_amount(0,300).perform()
        

hunting = True
page_numbers = driver.find_elements(By.CLASS_NAME, 'artdeco-pagination__indicator')
last_number = int(page_numbers[-1].text)

while hunting == True:
    for i in range(1, last_number):
        job_hunt()
        time.sleep(2)
        # on_screen_numbers = driver.find_element(By.CLASS_NAME, 'artdeco-pagination__indicator')
        next_page = driver.find_element(By.XPATH, f'//*[@aria-label="Page {i+1}"]')
        next_page.click()
        time.sleep(2)
        if i == last_number:
            hunting = False

print("Job Done!")