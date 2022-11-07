from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedrive_directory = "C:/Users/lutimoth/Documents/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(service=Service(chromedrive_directory))

# driver.get("http://secure-retreat-92358.herokuapp.com/")

# first_name = driver.find_element(By.NAME, 'fName')
# first_name.send_keys("Timothy")

# last_name = driver.find_element(By.NAME, 'lName')
# last_name.send_keys("Lu")

# email_input = driver.find_element(By.NAME, 'email')
# last_name.send_keys("lutimoth@gmail.com")

# button = driver.find_element(By.CSS_SELECTOR, "button.btn")
# button.click()


### --- COOKIE CLICKER AUTOPLAY --- ###

driver.get('http://orteil.dashnet.org/experiments/cookie/')