from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3344848896&f_AL=true&f_BE=%5B%5D&f_C=%5B%5D&f_E=%5B%5D&f_EA=%5B%5D&f_F=%5B%5D&f_FCE=%5B%5D&f_I=%5B%5D&f_JC=%5B%5D&f_JIYN=%5B%5D&f_JT=%5B%5D&f_PP=%5B%5D&f_SB2=%5B%5D&f_T=%5B%5D&f_WT=%5B%5D&keywords=data%20scientist&sortBy=R'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chromedrive_directory = "C:/Users/lutimoth/Documents/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(service=Service(chromedrive_directory))

driver.get(URL)

time.sleep(10)

signin_button = driver.find_element(By.CSS_SELECTOR, "a.nav__button-secondary")
signin_button.click()

time.sleep(30)