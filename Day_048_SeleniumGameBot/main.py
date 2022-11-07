from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chromedrive_directory = "C:/Users/lutimoth/Documents/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(service=Service(chromedrive_directory))

driver.get("https://en.wikipedia.org/wiki/Main_Page")
number_of_articles = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(number_of_articles.text)

driver.quit()