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

PROMISED_DOWN = os.getenv("PROMISED_DOWN")
PROMISED_UP = os.getenv("PROMISED_UP")
CHROME_DRIVER_PATH = os.getenv("CHROME_PATH")
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PW")
URL = 'https://www.speedtest.net/'

class InternetSpeedTwitterBot:

    def __init__(self,driver_path) -> None:
        self.driver = webdriver.Chrome(service=Service(executable_path=driver_path))
        self.down = 0
        self.up = 0
    
    def get_internet_speed(self):
        self.driver.get(URL)
        time.sleep(2)
        self.go_button = self.driver.find_element(By.CSS_SELECTOR, 'a.js-start-test')
        self.go_button.click()
        time.sleep(50)
        # self.close_button = self.driver.find_element(By.CLASS_NAME, 'close-btn')
        # self.close_button.click()
        # time.sleep(3)
        self.down = self.driver.find_element(By.CLASS_NAME, 'download-speed')
        self.up = self.driver.find_element(By.CLASS_NAME, 'upload-speed')

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

bot.get_internet_speed()
print(f"down: {bot.down.text}")
print(f"up: {bot.up.text}")

bot.tweet_at_provider()