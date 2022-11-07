from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chromedrive_directory = "C:/Users/lutimoth/Documents/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(service=Service(chromedrive_directory))

driver.get("https://www.amazon.com")