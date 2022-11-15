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


class InternetSpeedTwitterBot:

    def __init__(self,driver_path) -> None:
        self.driver = webdriver.Chrome(service=Service(executable_path=driver_path))
        self.down = 0
        self.up = 0
    
    def get_internet_speed(self):
        speed_url = 'https://www.speedtest.net/'
        self.driver.get(speed_url)
        time.sleep(2)
        self.go_button = self.driver.find_element(By.CSS_SELECTOR, 'a.js-start-test')
        self.go_button.click()
        time.sleep(50)
        # self.close_button = self.driver.find_element(By.CLASS_NAME, 'close-btn')
        # self.close_button.click()
        # time.sleep(3)
        self.down = self.driver.find_element(By.CLASS_NAME, 'download-speed')
        self.up = self.driver.find_element(By.CLASS_NAME, 'upload-speed')

    def tweet_at_provider(self, down, up):
        twitter_url = 'https://www.twitter.com/home'
        self.driver.get(twitter_url)
        time.sleep(2)
        self.login = self.driver.find_element(By.TAG_NAME, 'input')
        self.login.send_keys(TWITTER_EMAIL)
        self.next = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        self.next.click()
        time.sleep(2)
        self.pw = self.driver.find_element(By.NAME, 'password')
        self.pw.send_keys(TWITTER_PASSWORD)
        self.login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        self.login_button.click()
        time.sleep(2)
        self.tweet = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        self.tweet.click()
        self.tweet.send_keys(f"Hey, Internet Provider! I'm supposed to get {PROMISED_DOWN} and {PROMISED_UP} but I am getting {down} and {up}! What gives?")
        self.send = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        self.send.click()

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

bot.get_internet_speed()
print(f"down: {bot.down.text}")
print(f"up: {bot.up.text}")

bot.tweet_at_provider(bot.down, bot.up)